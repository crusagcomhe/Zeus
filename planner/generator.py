import os, openai, json

openai.api_key = os.getenv("OPENAI_API_KEY", "demo-key")

def generate_plan(intent: str) -> dict:
    """Convert natural language -> infra blueprint (simplified)."""
    prompt = f"Convert user intent to JSON blueprint: {intent}"
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    try:
        return json.loads(resp.choices[0].message.content)
    except Exception:
        # fallback dummy plan
        return {"chain": "solana", "service": "fastapi", "intent": intent}
