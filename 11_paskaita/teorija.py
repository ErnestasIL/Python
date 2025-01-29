#-------funkcijos! Args---------
#
# def print_args(*args):
#     print(args)
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(type(args))
#
# print_args('Adomas', 'sausis', 1000)

#---------------------


def give_hello_to_names(*args):
    res = ''
    for name in args:
        res += f'Hello, {name}!\n'
    return res

print(give_hello_to_names('Ram', 'Bronius', 'Petras', 'Valda', 'Gin'))

# def multiply_all_by_num(numb, *args):
#     for elem in args:
#         print(elem * numb)
#
# multiply_all_by_num(2, 2, 3, 4, 5)

#-----------------























