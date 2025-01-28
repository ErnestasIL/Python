import datetime as dt
from  random import randint, choice


print(randint(1, 10))
print('---------')
print(choice(['banana', 'cherry', 'apple', 'pear']))
print('---------')

#---------------



print(f'Dabartine data ir laikas {dt.datetime.now().strftime("%Y-%m%d %H:%M:%S")}')