import os
from dotenv import load_dotenv
from src.api.client import PokeApiClient
from src.utils.logging import get_logger

def before_all(context):
    load_dotenv(dotenv_path=os.path.join("configs", "settings.env"), override=True)
    base_url = os.getenv("BASE_URL", "https://pokeapi.co/api/v2")
    context.client = PokeApiClient(base_url=base_url)
    context.logger = get_logger()
    context.evidence_dir = os.path.join("reports", "evidence")
    os.makedirs(context.evidence_dir, exist_ok=True)

def after_scenario(context, scenario):
    # Guarda evidencia mínima si falla
    if scenario.status.name == "failed" and hasattr(context, "last_response"):
        path = os.path.join(context.evidence_dir, f"{scenario.name}.json")
        with open(path, "wb") as f:
            f.write(context.last_response.content)
