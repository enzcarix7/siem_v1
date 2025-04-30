import schedule
import time
from datetime import datetime
from utils import collect_logs, analyze_logs, send_alert

# Function to check logs and send alerts
def job():
    logs = collect_logs()
    errors = analyze_logs(logs)
    if errors:
        for error in errors:
            send_alert(error)

# Schedule the job to run every 5 minutes
schedule.every(5).minutes.do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
