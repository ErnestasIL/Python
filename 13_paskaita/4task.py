#1task
import datetime

first_date = datetime.datetime(2023, 1, 1)
second_date = datetime.datetime(2024, 1, 1)
date_res = second_date - first_date
print(date_res)

#2task

current_date = datetime.datetime.now()
future_date = datetime.timedelta(days=90)
res = current_date + future_date
print(f'Data po 90 dienu bus: {res}')

#3task

milenium_date = datetime.datetime(2000, 1, 1)

res2 = current_date - milenium_date

print(f'days: {res2.days}d')
print(f'hours(using seconds): {round(res2.seconds / 3600)}h')
print(f'hours(using total_seconds): {round(res2.total_seconds() / 3600)}h')
print(f'total seconds: {round(res2.total_seconds())}s')