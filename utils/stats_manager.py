import json
import os

class StatsManager:

    def __init__(self, path="data/stats.json"):
        self.path = path
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.path):
            self._initialize()

    def _initialize(self):
        default = {
            "tasks_completed": 0,
            "errors": 0,
            "files_organized": 0,
            "emails_sent": 0,
            "pages_scraped": 0
        }
        with open(self.path, "w") as f:
            json.dump(default, f, indent=4)

    def load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def update(self, key, value=1):
        data = self.load()
        data[key] += value
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)
