# openverse.py

import requests
from requests.exceptions import HTTPError
from pyopenverse.config import OPENVERSE_URL, FUNCTION_URLS
from pyopenverse.auth import AuthManager


class PyOpenverse:
    def __init__(self, client_id=None, client_secret=None) -> None:
        self.auth_manager = AuthManager(client_id, client_secret)

    def register(self, name: str, description: str, email: str):
        self.auth_manager.register(name, description, email)

    def img_search(
        self,
        query: str,
        page: int = 1,
        page_size: int = 500,
        license_type="commercial",
        aspect_ratio: str = "square,wide",
        size: str = "large",
    ):
        """
        Refer to https://api.openverse.engineering/v1/#tag/images/operation/images_search
        Args:
            page(int): 1~20
            page_size(int): <= 500
            license_type(str): all, all-cc, commercial, and modification(should be comma-separated)
            aspect_ratio(str): square, tall, and wide(should be comma-separated)
        Return:
            List of image URLs
        """
        if page > 20:
            print("No more page.")
            return None

        if page_size > 500:
            print(f"Exceed Maximum page size:{page_size}, should be <= 500.")
            page_size = 500

        headers = self.auth_manager.get_headers()  # curl headers
        params = {
            "q": query,
            "page": page,
            "page_size": page_size,
            "license_type": license_type,
            "aspect_ratio": aspect_ratio,
            "size": size,
        }
        url = OPENVERSE_URL + FUNCTION_URLS["img_search"]  # curl link
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            output = response.json()
            return [result["url"] for result in output["results"]]  # return imgs
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    def get_info(self):
        return self.auth_manager.get_info()
