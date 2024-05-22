# auth.py

import requests
from requests.exceptions import HTTPError
from datetime import datetime, timedelta
from dotenv import load_dotenv, set_key
import os
from config import OPENVERSE_URL, FUNCTION_URLS, ENV_FILE


class AuthManager:
    def __init__(self, client_id=None, client_secret=None) -> None:
        load_dotenv(ENV_FILE)
        self.client_id = client_id or os.getenv("OPENVERSE_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("OPENVERSE_CLIENT_SECRET")
        self.token = ""
        self.token_expiry = datetime.now()

    def register(self, name: str, description: str, email: str):
        print("Registering for API access...")
        url = OPENVERSE_URL + FUNCTION_URLS["register"]
        data = {
            "name": name,
            "description": description,
            "email": email,
        }
        try:
            response = requests.post(
                url, json=data, headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            registration_data = response.json()
            self.client_id = registration_data["client_id"]
            self.client_secret = registration_data["client_secret"]
            self._save_credentials()
            print("Registration successful.")
            print(f"Client ID: {self.client_id}")
            print(f"Client Secret: {self.client_secret}")
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    def _save_credentials(self):
        set_key(ENV_FILE, "OPENVERSE_CLIENT_ID", self.client_id)
        set_key(ENV_FILE, "OPENVERSE_CLIENT_SECRET", self.client_secret)

    def get_token(self):
        print("Requesting Token...")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        url = OPENVERSE_URL + FUNCTION_URLS["token"]
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        try:
            response = requests.post(url, data=data, headers=headers)
            response.raise_for_status()
            token_data = response.json()
            self.token = token_data["access_token"]
            expires_in = token_data["expires_in"]
            self.token_expiry = datetime.now() + timedelta(seconds=expires_in)
            print("Token received.")
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    def is_token_valid(self):
        return datetime.now() < self.token_expiry

    def get_headers(self):
        if not self.is_token_valid():
            self.get_token()
        return {"Authorization": f"Bearer {self.token}"}

    def get_info(self):
        url = OPENVERSE_URL + FUNCTION_URLS["info"]
        headers = self.get_headers()
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
