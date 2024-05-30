import psutil
import smtplib
from email.mime.text import MIMEText

print("Enter CPU THRESHOLD")
CPU_THRESHOLD = int(input())
print("Enter MEMORY THRESHOLD")
MEMORY_THRESHOLD = int(input())
print("Enter DISK THRESHOLD")
DISK_THRESHOLD = int(input())


def send_alert(subject, body):
    sender = "sender@email.com"
    recipient = "receiver@email.com"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP('localhost') as smtp:
        smtp.send_message(msg)


def monitor_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    if cpu_usage > CPU_THRESHOLD:
        send_alert("High CPU Usage Alert", f"CPU usage is {cpu_usage}%")

    if memory_usage > MEMORY_THRESHOLD:
        send_alert("High Memory Usage Alert", f"Memory usage is {memory_usage}%")

    if disk_usage > DISK_THRESHOLD:
        send_alert("Low Disk Space Alert", f"Disk usage is {disk_usage}%")

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")


import time
while True:
    monitor_system()
    time.sleep(60)