from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    print("定时任务执行中...")

# 创建调度器
scheduler = BlockingScheduler()

# 每天凌晨 1 点执行任务
scheduler.add_job(job, 'cron', hour=1, minute=0)

# 启动调度器
scheduler.start()