import requests
from bs4 import BeautifulSoup
import random

class WebScraper:

    def __init__(self, user_agents):
        self.user_agents = user_agents

    def scrape_titles(self, url):
        headers = {"User-Agent": random.choice(self.user_agents)}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        return [h.text.strip() for h in soup.find_all("h1")]
