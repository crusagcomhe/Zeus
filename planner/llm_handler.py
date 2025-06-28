import os
import json

config = json.load(open("zeus/agent_config.json"))
provider = config["model_provider"]
model_info = config["model_config"][provider]

if provider == "openai":
    api_key = os.getenv(model_info["api_key_env"])
    # use OpenAI SDK
elif provider == "anthropic":
    api_key = os.getenv(model_info["api_key_env"])
    # use Anthropic SDK
elif provider == "local":
    # connect to local LLM via HTTP
    host = model_info["host"]
