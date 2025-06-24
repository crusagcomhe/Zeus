"""
adapters/solana/indexer.py
-------------------------------------------------
Light-weight wallet indexer for Solana. Designed
for integration with Zeus' wallet-audit flow.

Usage (script mode):
    python -m adapters.solana.indexer <WALLET> --limit 50 --net devnet
"""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Confirmed

DEFAULT_ENDPOINTS = {
    "devnet": "https://api.devnet.solana.com",
    "mainnet": "https://api.mainnet-beta.solana.com",
}


class TxClassifier:
    """Very naive instruction classifier."""

    @staticmethod
    def classify(ix: Dict[str, Any]) -> str:
        program = ix.get("program")
        if program == "system":
            return "system_transfer"
        if program == "spl-token":
            return "spl_token_transfer"
        if program == "spl-associated-token-account":
            return "ata_create"
        if program and program.startswith("stake"):
            return "stake_op"
        # Fallback
        return program or "unknown"


async def fetch_tx_details(
    client: AsyncClient, sig: str
) -> Optional[Dict[str, Any]]:
    resp = await client.get_transaction(sig, commitment=Confirmed)
    value = resp.value
    if not value:
        return None
    meta = value.get("meta", {})
    instructions = []
    for ix in value["transaction"]["message"]["instructions"]:
        kind = TxClassifier.classify(ix)
        instructions.append(dict(kind=kind, raw=ix))
    return {
        "signature": sig,
        "slot": value.get("slot"),
        "fee": meta.get("fee", 0),
        "success": not bool(meta.get("err")),
        "instructions": instructions,
    }


async def index_wallet(
    wallet: str,
    limit: int = 100,
    endpoint: str = DEFAULT_ENDPOINTS["mainnet"],
) -> List[Dict[str, Any]]:
    pub = PublicKey(wallet)
    client = AsyncClient(endpoint, commitment=Confirmed)

    sig_resp = await client.get_signatures_for_address(pub, limit=limit)
    sigs = [x.signature for x in sig_resp.value]

    # Pull tx details concurrently
    tasks = [asyncio.create_task(fetch_tx_details(client, s)) for s in sigs]
    results = [r for r in await asyncio.gather(*tasks) if r is not None]

    await client.close()
    return results


# --------------------------------------------------------------------------- #
# Script entry point for ad-hoc usage
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Solana wallet transaction indexer")
    parser.add_argument("wallet", help="Public key to index")
    parser.add_argument("--limit", type=int, default=50, help="Txn limit (default 50)")
    parser.add_argument(
        "--net",
        choices=["devnet", "mainnet", "custom"],
        default="devnet",
        help="Network",
    )
    parser.add_argument("--endpoint", help="Custom RPC endpoint (if --net custom)")

    args = parser.parse_args()

    rpc = (
        args.endpoint
        if args.net == "custom"
        else DEFAULT_ENDPOINTS.get(args.net, DEFAULT_ENDPOINTS["devnet"])
    )

    data = asyncio.run(index_wallet(args.wallet, args.limit, rpc))
    out = Path.cwd() / f"{args.wallet[:6]}_index.json"
    out.write_text(json.dumps(data, indent=2))
    print(f"Indexed {len(data)} txs → {out}") 
