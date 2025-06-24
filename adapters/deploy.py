from solana.rpc.async_api import AsyncClient
from solana.keypair import Keypair
from solana.rpc.commitment import Confirmed
import asyncio

class SolanaDeployer:
    """Demo deployer: airdrops and returns a fake program id."""

    async def _async_deploy(self, plan):
        client = AsyncClient("https://api.devnet.solana.com", commitment=Confirmed)
        kp = Keypair()
        await client.request_airdrop(kp.public_key, 1_000_000_000)
        await client.close()
        return {"program_id": str(kp.public_key), "plan": plan}

    def deploy(self, plan):
        return asyncio.run(self._async_deploy(plan))
