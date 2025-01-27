# funkcijos:
# user_name = input('Your name:')

# print(f'Hello {user_name}')

# text = 'ABCcba123'
#
# res = len(text)
#
# print(res)

# for skaicius in range(1, 6):
#     print(skaicius)


# for even_numbers in range(2, 21, 2):
#     print(even_numbers)
#
# total = sum(number ** 2 for number in range(2, 21, 2))
#
# print(total)
#
# for number in range(10, 0, -1):
#     print(number)


# print('S', 'K', 'P', 'L', sep=' | ')
#
# print('TASK', end='||')
#
# print('S K P L', sep=' | ')
#
# print(f'{"S"} {"K"} {"P"} {"L"}', sep='|')

# listas = ['abs', 123, True]
#
# for elem in listas:
#     if type(elem) == str:
#         print(elem.upper())
#     elif type(elem) == int:
#         print(elem % 2)
#     elif type(elem) == bool and elem == True:
#         print('You can login')

#                                                       !!!!task!!!!

fruits = ['Oboluolys', 'Kriause', 'Bananas', 'Vysnia']
print(*fruits, sep=' | ')

print('1)Oboluolys', '2)Kriause', '3)Bananas', '4)Vysnia')

result = ", ".join(f"{i+1}) {fruit}" for i, fruit in enumerate(fruits))
print(result)

print("banana", end="||||")
print("banana", end="||||")
print("banana")


random_list = [123, 'Labas', True, 45.666, None]
for elem in random_list:
    if type(elem) == int:
        print(elem * 10)
    elif type(elem) == str:
        print(elem.upper())
    elif type(elem) == bool:
        print('True or False Found')
    elif type(elem) == float:
        print(round(elem, 2))
    else:
        print(f'undifined : {type(elem)}')

