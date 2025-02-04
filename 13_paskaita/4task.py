#1task
from _datetime import datetime,timedelta

first_date = datetime(2023, 1, 1)
second_date = datetime(2024, 1, 1)
date_res = second_date - first_date
print(f'skirtumas: {date_res.days}')

#2task

current_date = datetime.now()
future_date = timedelta(days=90)
res = current_date + future_date
print(f"Data po 90 dienu bus: {res.strftime('%Y-%m-%d')}")

#3task

millennium_date = datetime(2000, 1, 1)

res2 = current_date - millennium_date

print(f'days: {res2.days}d')
print(f'hours(using seconds): {(res2.seconds // 3600)}h')
print(f'hours(using total_seconds): {(res2.total_seconds() // 3600)}h')
print(f'total seconds: {int(res2.total_seconds())}s')