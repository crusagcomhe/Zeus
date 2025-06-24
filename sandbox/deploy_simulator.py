def simulate_plan(plan: dict) -> dict:
    """Pretend to build Docker image and ensure success."""
    # In reality you'd build & inspect; here we always succeed
    return {"status": "success", "plan": plan}
