import json
from datetime import datetime

class Exporter:

    def export_json(self, report):
        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump({"report": report}, f, indent=4)

    def export_txt(self, report):
        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(report)
