# while True:
#     number1 = input('Iveskite skaiciu: ')
#     number2 = input('Iveskite skaiciu is kurio norite padalinti: ')
#
#     try:
#         skaicius = int(number1)
#         daliklis = int(number2)
#         res = skaicius / daliklis
#         print(f'Rezultatas: {res}')
#     except ZeroDivisionError as zero:
#         print(f'Ivedete nuli ir gavote error: {zero}')
#     except ValueError as val:
#         print(f'Ivedete ne skaiciu ir gavote error: {val}')
#
#     print('-------------------')

import time
time_limit = 3

def get_password():
   print("Please enter your password:")
   start_time = time.time()
   password = input("Password: ")
   end_time = time.time()

   time_taken = end_time - start_time
   if time_taken < time_limit:
       print("Password incorrect! Try again.")
   else:
       print("Password submitted successfully.")
get_password()

