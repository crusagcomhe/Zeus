Zeus – Autonomous Web3 Deployment Agent

Zeus is an AI‑assisted, local‑first framework that transforms plain‑language requirements into complete, reproducible infrastructure for decentralised applications.  It generates Docker‑based blueprints, audits Solana wallets, and performs sandboxed dry‑run simulations—helping builders ship production‑ready deployments with confidence and zero cloud lock‑in.

Table of Contents

Key Objectives

Feature Overview

System Architecture

Directory Structure

Dependency Management

Installation

Usage Examples

Documentation

Roadmap

Contributing

Security

Troubleshooting

License

Key Objectives

Goal

Description

Reduce DevOps toil

Convert human intent into infrastructure‑as‑code automatically.

Safer on‑chain launches

Analyse Solana wallets for risk and mis‑deploy patterns.

Local‑first workflows

All generation and simulation run on your machine; no vendor lock‑in.

Extensibility

Add new chains or exporters through the plugin API.

Feature Overview

Category

Capability

Status

LLM planner

Natural‑language prompt → Dockerfile · GitHub Actions · Terraform

Stable

Dry‑run simulator

Containerised build and health checks

Stable

Solana wallet audit

Transaction risk scoring, token map, fee analysis

Stable

Anchor auto‑deploy

Compile and push smart contracts to Devnet

Beta

EVM adapters

Hardhat / Foundry pipeline

Alpha

System Architecture

flowchart TD
  A[User Prompt] --> B[LLM Planner]
  B --> C[MCP Config]
  C --> D[Dry‑Run Simulator]
  D --> E[Artifact Store]
  C --> F[Chain Adapter]
  F --> G[Solana Devnet]
  D --> H[Report Engine]
  subgraph Audit
    I[Wallet Scanner] --> B
  end

Each component is isolated; adapters can be swapped via Python entry‑points.

Directory Structure

Zeus/
├─ cli/                   Command‑line entry points
├─ agent_core/           LLM planner · simulator · reporters
├─ chain/
│  ├─ solana/            Devnet deployer
│  └─ evm/               Hardhat placeholder
├─ tools/                Wallet audit, exporters, helpers
├─ docs/                 Additional documentation (MkDocs site)
├─ tests/                Pytest suite
├─ pyproject.toml        Modern build + dependency metadata
├─ requirements.txt      Locked minimal runtime set
└─ README.md

Dependency Management

Primary file: pyproject.toml – declared dependencies, metadata, build backend.

Secondary lock: requirements.txt – exact versions for CI images.

To add a library:

[project.dependencies]
rich = "*"

then run pip install -e ..

Installation

Prerequisites

Python 3.10+

Docker 20.10+

(Optional) Rust toolchain + Anchor CLI

Steps

git clone https://github.com/YOUR_USER/Zeus.git
cd Zeus
pip install -e .

Usage Examples

# generate and simulate a deployment
zeus deploy --intent "Deploy a FastAPI backend with Solana NFT indexer"

# audit a wallet before launch
zeus wallet-audit H7Us7PXnXJ...

Outputs:

Generated Dockerfile, compose, scripts

Dry‑run build logs and health report

Wallet fee burn, suspicious tx flags, token categorisation

Documentation

Full reference lives in the docs folder and is published automatically to GitHub Pages via the docs.yml workflow:

docs/llm.md – prompt grammar, planner description

docs/simulator.md – container sandbox internals

docs/solana.md – RPC endpoints, audit heuristics

Run locally:

pip install mkdocs-material
mkdocs serve

Roadmap

Release

ETA

Highlights

v0.5

Aug 2025

Anchor full compile & Devnet deploy, Render exporter

v0.6

Dec 2025

Web playground GUI, railway integration

v1.0

Q2 2026

zk‑attested deploy flow, plugin marketplace, Cosmos adapter

Contributing

Fork → git checkout -b feat/<topic>

Run pytest and pre‑commit

Follow Conventional Commits and Black formatting

Submit PR with descriptive title + screenshots/logs

See CONTRIBUTING.md for full guidelines.

Security

Docker network set to none during simulation

No secrets persisted – env vars passed at runtime only

Wallet RPC is read‑only; no private‑key handling

Planned: zk‑proof deploy attestations (Q2 2026)

Troubleshooting

Symptom

Solution

Docker build times out

Increase Docker memory ≥ 4 GB

RPC 429 rate limit

Set custom RPC endpoint via SOLANA_RPC env

LLM quota exceeded

Export OPENAI_API_KEY with higher quota

License

MIT License © 2025 crusagcomhe

Zeus is free for commercial and non‑commercial use with attribution.

