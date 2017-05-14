from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
def superProgram():
    subprocess.call("python /Users/mayurjain/Documents/zomatoNegativeFeedback.py 1",shell=True)

scheduler = BlockingScheduler()
scheduler.add_job(superProgram, 'interval', hours=1)
scheduler.start