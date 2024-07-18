import os

from dotenv import load_dotenv

load_dotenv()


class Credentials:

    @classmethod
    def retell_api_key(cls) -> str:
        return os.getenv("RETELL_API_KEY")

    @classmethod
    def retell_webhook_url(cls) -> str:
        return os.getenv("RETELL_WEBHOOK_URL")
