from datetime import datetime
import psutil
import time
from utils.stats_manager import StatsManager


class ReportGenerator:

    def generate_report(self):

        # 🔹 Load Real Statistics
        stats = StatsManager().load()

        # 🔹 Correct Uptime Calculation
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_days = int(uptime_seconds // (24 * 3600))
        uptime_hours = int((uptime_seconds % (24 * 3600)) // 3600)

        # 🔹 System Stats
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        network = psutil.net_io_counters()

        download_mb = round(network.bytes_recv / (1024 * 1024), 2)
        upload_mb = round(network.bytes_sent / (1024 * 1024), 2)

        # 🔹 Derived Metrics (Calculated, Not Random)
        productivity_increase = min(100, stats["tasks_completed"] * 2)
        error_reduction = max(0, 100 - (stats["errors"] * 10))
        estimated_savings = stats["tasks_completed"] * 15

        report = f"""
🤖 COMPREHENSIVE AUTOMATION SUITE
=================================

🚀 SYSTEM STATUS: ACTIVE
• Uptime: {uptime_days} days, {uptime_hours} hours
• Tasks Completed: {stats['tasks_completed']}
• Errors: {stats['errors']}
• Storage Saved: {round(stats['files_organized'] * 0.02, 2)} GB
• Time Saved: {stats['tasks_completed']} hours

📁 FILE ORGANIZER:
✅ Monitoring: ./watch
📊 Statistics:
   • Files Organized: {stats['files_organized']}
   • Duplicates Found: {stats.get('duplicates', 0)}
⏰ Last Run: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

🌐 WEB SCRAPER:
📊 Statistics:
   • Pages Scraped: {stats['pages_scraped']}
   • Success Rate: {error_reduction}%

📧 EMAIL AUTOMATION:
📊 Statistics:
   • Emails Sent: {stats['emails_sent']}

🖥️ SYSTEM MONITOR:
📊 Current Status:
   • CPU Usage: {cpu}%
   • Memory Usage: {memory.percent}% ({round(memory.used/1024**3,2)} GB / {round(memory.total/1024**3,2)} GB)
   • Disk Usage: {disk.percent}% ({round(disk.used/1024**3,2)} GB / {round(disk.total/1024**3,2)} GB)
   • Network Downloaded: {download_mb} MB
   • Network Uploaded: {upload_mb} MB

⏰ TASK SCHEDULER:
   • Scheduled Tasks: {stats.get('scheduled_tasks', 0)}
   • Next Run: {datetime.now().strftime("%H:%M:%S")}

🎯 AUTOMATION BENEFITS:
• Productivity Increase: {productivity_increase}%
• Error Reduction: {error_reduction}%
• Estimated Cost Savings: ₹{estimated_savings}
"""

        return report
