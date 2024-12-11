import requests

from utilities.base_class import BaseClass


class TestAPI(BaseClass):
    def test_api(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        print(response.text)
        assert response.status_code == 200
        assert response.json()["id"] == 1
