from apscheduler.schedulers.background import BackgroundScheduler
from notifier import notify

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(notify, 'cron', minute=0)
    scheduler.start()