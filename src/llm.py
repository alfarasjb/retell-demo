import requests
from src.definitions.credentials import Credentials
from src.definitions import endpoints


class LLMClient:
    def __init__(self):
        self.base_url = 'https://api.retell.com'
        self._headers = {
            "Authorization": f"Bearer {Credentials.retell_api_key()}",
            # "Content-Type": "application/json"
        }

    def list_retell_llms(self):
        endpoint = self.base_url + endpoints.LIST_LLMS
        response = requests.get(endpoint, headers=self._headers)

    def list_retell_agents(self):
        endpoint = self.base_url + endpoints.LIST_AGENTS
        response = requests.get(endpoint, headers=self._headers)


