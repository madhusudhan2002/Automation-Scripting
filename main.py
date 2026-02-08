from utils.logger import setup_logger
from utils.config_loader import load_config
from modules.file_organizer import FileOrganizer
from modules.web_scraper import WebScraper
from modules.api_client import APIClient
from modules.email_automation import EmailAutomation
from modules.system_monitor import SystemMonitor
from modules.scheduler import TaskScheduler
from modules.network_tools import NetworkTools
from modules.report_generator import ReportGenerator
from gui.app import App

import logging


def main():
    try:
        # 🔹 Setup Logging
        setup_logger()
        logging.info("Starting Automation Suite...")

        # 🔹 Load Configuration
        config = load_config()

        # 🔹 Initialize Modules
        organizer = FileOrganizer(
            config["file"]["watch_folder"],
            config["file"]["organized_folder"]
        )

        scraper = WebScraper(config["scraper"]["user_agents"])
        api = APIClient(config["api"]["base_url"])
        emailer = EmailAutomation(config["email"])
        monitor = SystemMonitor()
        scheduler = TaskScheduler()
        network = NetworkTools()

        # 🔹 Start Scheduler
        scheduler.add_daily(organizer.organize, "00:00")
        scheduler.start()

        # 🔹 Generate Report
        reporter = ReportGenerator()
        print(reporter.generate_report())

        print("Automation Suite Running...")

        # 🔹 Start GUI
        app = App()
        app.run()

    except KeyboardInterrupt:
        print("\nAutomation Suite stopped safely by user.")
        logging.info("Automation Suite stopped by user.")

    except Exception as e:
        print("\nUnexpected error occurred:", e)
        logging.error(f"Unexpected error: {e}")

from gui.dashboard import Dashboard
...
app = Dashboard()
app.run()

if __name__ == "__main__":
    main()
