#----------datetime

import datetime

# dt_res = datetime.datetime.today()
# print(dt_res)
# print(dt_res.year)
# print(dt_res.month)
# print(dt_res.day)
# print(dt_res.hour)
# print(dt_res.minute)
# print(dt_res.second)
# print(dt_res.microsecond)


my_datetime = datetime.datetime(2011, 12, 31, 23, 59, 59)

print(my_datetime)

time_from_2000 = datetime.datetime.today() - datetime.datetime(2000, 1, 1)
print(time_from_2000)




















