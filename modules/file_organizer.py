import os
import shutil
from datetime import datetime
from utils.stats_manager import StatsManager

stats = StatsManager()
stats.update("files_organized")
stats.update("tasks_completed")

class FileOrganizer:

    CATEGORIES = {
        "Documents": [".pdf", ".docx", ".txt"],
        "Images": [".jpg", ".png", ".jpeg"],
        "Code": [".py", ".js", ".html"],
        "Videos": [".mp4", ".avi"],
        "Archives": [".zip", ".rar"]
    }

    def __init__(self, watch, organized):
        self.watch = watch
        self.organized = organized
        os.makedirs(self.organized, exist_ok=True)

    def organize(self):
        for file in os.listdir(self.watch):
            path = os.path.join(self.watch, file)

            if os.path.isfile(path):
                ext = os.path.splitext(file)[1].lower()
                moved = False

                for category, extensions in self.CATEGORIES.items():
                    if ext in extensions:
                        dest = os.path.join(self.organized, category)
                        os.makedirs(dest, exist_ok=True)

                        new_path = os.path.join(dest, file)

                        # Handle duplicate file names
                        if os.path.exists(new_path):
                            base, ext = os.path.splitext(file)
                            timestamp = datetime.now().strftime("%H%M%S")
                            file = f"{base}_{timestamp}{ext}"
                            new_path = os.path.join(dest, file)

                        shutil.move(path, new_path)
                        moved = True
                        break

                if not moved:
                    other = os.path.join(self.organized, "Others")
                    os.makedirs(other, exist_ok=True)
                    shutil.move(path, os.path.join(other, file))
