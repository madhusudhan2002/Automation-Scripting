from flask import Flask, jsonify
from utils.stats_manager import StatsManager
import psutil
from datetime import datetime
import time

app = Flask(__name__)

# -------------------------------
# Utility: Standard API Response
# -------------------------------
def api_response(data, message="success"):
    return jsonify({
        "status": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": data
    })

# -------------------------------
# Home Route
# -------------------------------
@app.route("/")
def home():
    return """
    <h1>🚀 Automation Suite API</h1>
    <p>Status: Running</p>
    <ul>
        <li><a href="/api/v1/report">View Full Report</a></li>
        <li><a href="/api/v1/stats">View Raw Stats</a></li>
        <li><a href="/api/v1/system">View System Info</a></li>
        <li><a href="/api/v1/health">Health Check</a></li>
    </ul>
    """

# -------------------------------
# Structured Report Endpoint
# -------------------------------
@app.route("/api/v1/report")
def report():
    stats = StatsManager().load()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    uptime_seconds = time.time() - psutil.boot_time()

    return api_response({
        "system_status": {
            "uptime_days": int(uptime_seconds // (24 * 3600)),
            "uptime_hours": int((uptime_seconds % (24 * 3600)) // 3600),
            "tasks_completed": stats["tasks_completed"],
            "errors": stats["errors"]
        },
        "file_organizer": {
            "files_organized": stats["files_organized"],
            "duplicates": stats.get("duplicates", 0)
        },
        "web_scraper": {
            "pages_scraped": stats["pages_scraped"]
        },
        "email_automation": {
            "emails_sent": stats["emails_sent"]
        },
        "system_monitor": {
            "cpu_percent": psutil.cpu_percent(),
            "memory_percent": memory.percent,
            "memory_used_gb": round(memory.used / (1024**3), 2),
            "memory_total_gb": round(memory.total / (1024**3), 2),
            "disk_percent": disk.percent,
            "disk_used_gb": round(disk.used / (1024**3), 2),
            "disk_total_gb": round(disk.total / (1024**3), 2)
        }
    })

# -------------------------------
# Statistics Endpoint
# -------------------------------
@app.route("/api/v1/stats")
def stats():
    return api_response(StatsManager().load())

# -------------------------------
# System Monitoring Endpoint
# -------------------------------
@app.route("/api/v1/system")
def system():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return api_response({
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": memory.percent,
        "disk_percent": disk.percent
    })

# -------------------------------
# Health Endpoint
# -------------------------------
@app.route("/api/v1/health")
def health():
    return api_response({
        "service": "Automation Suite API",
        "version": "1.0",
        "status": "healthy"
    })

# -------------------------------
# Error Handling
# -------------------------------
@app.errorhandler(404)
def not_found(error):
    return api_response({"error": "Endpoint not found"}, "error"), 404

@app.errorhandler(500)
def internal_error(error):
    return api_response({"error": "Internal server error"}, "error"), 500

# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":
    app.run(port=5000, debug=True)
