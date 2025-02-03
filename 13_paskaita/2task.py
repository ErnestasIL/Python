import datetime
set_date = datetime.datetime(1995, 6, 14, 15, 30)
print(set_date)
second_date = datetime.datetime(2023, 1, 1)
print(second_date.strftime('%Y-%m-%d'))

day_from_2000 = datetime.datetime.today() - datetime.datetime(2000, 1, 1)

print(f'Praejo {day_from_2000.days} dienu, nuo 2000-01-01')