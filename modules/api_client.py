import requests

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_public_repos(self, username):
        url = f"{self.base_url}/users/{username}/repos"
        response = requests.get(url)
        return [repo["name"] for repo in response.json()]
