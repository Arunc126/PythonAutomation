import requests

from utilities.base_class import BaseClass


class TestAPI(BaseClass):
    def test_api(self):
        logger = self.get_logger()
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        logger.info(response.text)
        assert response.status_code == 200
        assert response.json()["id"] == 1

    def test_api_negative(self):
        logger = self.get_logger()
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        logger.info(response.text)
        assert response.status_code == 400
