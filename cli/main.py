import json, click, asyncio
from rich import print
from planner.generator import generate_plan
from sandbox.deploy_simulator import simulate_plan
from adapters.solana.deploy import SolanaDeployer

@click.command()
@click.option("--intent", "-i", prompt=True, help="Plain-language deployment goal")
def main(intent: str):
    """Entry-point for Zeus CLI."""
    plan = generate_plan(intent)
    print("[bold cyan]Blueprint generated[/] -> running dry-run simulation...")
    result = simulate_plan(plan)
    if result["status"] != "success":
        print("[red]Simulation failed[/]")
        return
    deployer = SolanaDeployer()
    deployed = deployer.deploy(plan)
    print(json.dumps(deployed, indent=2))

if __name__ == "__main__":
    main()
