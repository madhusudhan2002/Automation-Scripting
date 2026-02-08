import schedule
import time
import threading

class TaskScheduler:

    def __init__(self):
        self.running = False

    def add_daily(self, task, time_str):
        schedule.every().day.at(time_str).do(task)

    def start(self):
        def run():
            while True:
                schedule.run_pending()
                time.sleep(1)

        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()
