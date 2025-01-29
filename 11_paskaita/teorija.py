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


# def give_hello_to_names(*args):
    # res = ''
    # for name in args:
        # res += f'Hello, {name}!\n'
    # return res

# print(give_hello_to_names('Ram', 'Bronius', 'Petras', 'Valda', 'Gin'))

# def multiply_all_by_num(numb, *args):
#     for elem in args:
#         print(elem * numb)
#
# multiply_all_by_num(2, 2, 3, 4, 5)

#-----------------

# def multiply_all_by_numb(numb: int, *args, text: str='* daugyba') -> None:
#     for elem in args:
#         print(f'{numb * elem} {text}')
#
# multiply_all_by_numb(7, 10, 11, 50)
# multiply_all_by_numb(7, 10, 11, 50, text= '***')
#--------------------
#
# def multiply_all_by_numb(numb: int, *args, info=False):
#     multiply_numbs = [elem * numb for elem in args]
#     if info:
#         print(f'daugiklis: {numb}, args: {args}, rezultatas: {multiply_numbs}')
#     return multiply_numbs
#
# res = multiply_all_by_numb(7, 10, 11, 50)
# print(res)
#
# res = multiply_all_by_numb(7, 10, 11, 50, info=True)
# print(res)

# def check_type_of_args(*args:(int, float, str)):
#     for arg in args:
#         print(type(arg))
#
# check_type_of_args(1, '2', 34, '58', 99.99)

#-------------kwargs----------------
#
# def print_kwargs(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
# print_kwargs(pirmas = 1, antras = 2)

# def print_list(listas, skirtukas=' ', eilutes_pabaiga='\n'):
#     for elem in listas:
#         print(elem, 'men.', sep=skirtukas, end=eilutes_pabaiga)
list_duomenu = ['sausis', 'vasaris', 'kovas']
#
# print_list(list_duomenu)
# print_list(list_duomenu, skirtukas='|||', eilutes_pabaiga ='***\n')


def print_list(listas, **kwargs):
    for elem in listas:
        print(elem, 'men.', **kwargs)

# print_list(list_duomenu, sep='>>>')
print_list(list_duomenu, sep='>>>', end='---')













