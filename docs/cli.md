# CLI Reference

```bash
zeus deploy --intent "launch NFT rental protocol"
zeus wallet-audit <address>

### `docs/architecture.md`
```markdown
# System Architecture

```mermaid
flowchart LR
  A[Intention] --> B[LLM Planner]
  B --> C[Blueprint]
  C --> D[Simulation]
  D --> E[Deploy]

### `docs/adapters/solana.md`
```markdown
# Solana Adapter

Details about airdrop, devnet deploy, and Anchor workflow.
