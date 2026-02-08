import psutil

class SystemMonitor:

    def get_status(self):
        return {
            "CPU": psutil.cpu_percent(),
            "Memory": psutil.virtual_memory().percent,
            "Disk": psutil.disk_usage('/').percent
        }
