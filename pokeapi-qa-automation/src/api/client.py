import requests
from tenacity import retry, stop_after_attempt, wait_exponential

class PokeApiClient:
    def __init__(self, base_url: str, timeout: float = 10.0):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.timeout = timeout
        self.session.headers.update({"User-Agent": "pokeapi-qa-automation/1.0"})

    def set_timeout(self, timeout: float):
        self.timeout = timeout

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.2, min=0.2, max=1.5))
    def _get(self, path: str, params: dict | None = None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.get(url, params=params, timeout=self.timeout)

    def get_pokemon(self, pokemon: str | int):
        return self._get(f"pokemon/{pokemon}")

    def get_pokemon_list(self, limit=20, offset=0):
        return self._get("pokemon", params={"limit": limit, "offset": offset})
