import requests

class ExternalAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    def get_all(self):
        response = requests.get(self.BASE_URL)
        return response.json()

    def get_by_id(self, item_id: int):
        response = requests.get(f"{self.BASE_URL}/{item_id}")
        if response.status_code == 404:
            return None
        return response.json()

    def create(self, item: dict):
        response = requests.post(self.BASE_URL, json=item)
        return response.json()
