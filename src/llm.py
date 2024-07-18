import requests
from src.definitions.credentials import Credentials
from src.definitions import endpoints


class LLMClient:
    def __init__(self):
        self.base_url = 'https://api.retellai.com'
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

    def test_agent(self):
        agent_id = 'aac220f3cfc499062d26d51571cf0451'
        endpoint = self.base_url + endpoints.GET_AGENT + f"/{agent_id}"
        print(endpoint)
        print(self._headers)
        response = requests.get(endpoint, headers=self._headers)
        return response

if __name__ == "__main__":
    client = LLMClient()
    response = client.test_agent()
    print(response.status_code)