import datetime
#-----------------------

user_date = input("Įveskite datą formatu YYYY-MM-DD: ")

try:
    print(datetime.datetime.strptime(user_date, '%Y-%m-%d'))
except ValueError:
    print("Įvestas neteisingas datos formatas. Bandykite dar kartą su formatu YYYY-MM-DD.")
#--------------------

user_date2 = '2022-12-31, 23:59:59'
object_datetime = datetime.datetime(2022, 12, 31, 23, 59, 59)

print(object_datetime.strftime('%d/%m/%Y %H:%M:%S'))

formatted_date = object_datetime.strftime("%Y metų %B %d diena")

month_translation = {
    "January": "sausio",
    "February": "vasario",
    "March": "kovo",
    "April": "balandžio",
    "May": "gegužės",
    "June": "birželio",
    "July": "liepos",
    "August": "rugpjūčio",
    "September": "rugsėjo",
    "October": "spalio",
    "November": "lapkričio",
    "December": "gruodžio"
}

for eng, lt in month_translation.items():
    formatted_date = formatted_date.replace(eng, lt)

print(formatted_date)



