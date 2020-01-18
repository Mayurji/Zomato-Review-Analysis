**Import the two Libraries**
>from apscheduler.schedulers.blocking import BlockingScheduler

>import subprocess

**Create a function**
    Schedule a process to run the script

**Scheduler**
  >scheduler = BlockingScheduler()
  
  >scheduler.add_job(superProgram, 'interval', hours=1) // it will execute the program every one hour
  
  >scheduler.start()
