#---------------------- Funkcijos!!!!!

# def say_hello():
#     print('Hello user!')
#
# def say_bye():
#     ...
#
# say_hello()
#
#
# for i in range(10):
#     say_hello()

# name = 'Er'
#
# def create_greetings(user):
#     if not user:
#         return
#     res = f'greetings, {user}'
#     return res
#
# greetings = create_greetings(name)
#
# if greetings:
#     print(greetings)
# else:print('No user! oh no')

#----------------------------
#
# def say_hello_to_two(name1, name2):
#     if not name1 or not name2:
#         return
#     hello_string = f'hello to {name1} and Hello to {name2}'
#     return hello_string
#
# res = say_hello_to_two('Pranas', 'Jonas')
#
# print(res)

#----------------------------Numatyti argumentai:----------------

# def greet(name='Friend'):
#     print(f'Hello {name}!')

# greet('Erne')
# greet()
#
# def priimk_pacienta(pacientas, gydytojas='gyd. Pagalnutylenis'):
#     irasas_gyd_zurnale = f'Pacientas {pacientas}, prieme {gydytojas}'
#     return irasas_gyd_zurnale
#
#
# res = priimk_pacienta('Bronius')
# print(res)
#
# res = priimk_pacienta('Varvara')
# print(res)
#
# res = priimk_pacienta(
#     'Staska',
#     'gyd. Pakaitenis')
# print(res)
#


#-------------------------------

# def dalink_spec(sk1, sk2, iki_sveiko_sk=False):
#     if not iki_sveiko_sk:
#         return sk1 / sk2
#     return sk1 // sk2
#
# print(dalink_spec(777, 5, True))

# def button_modify_product(product, inform_client = False):
#     if not inform_client:
#         print('Product was modified succesfuly, by system!')
#     return product * 50
#
# button_modify_product('tapkes', True)
# button_modify_product('tapkes')

#--------------------------dokstringai/


# def say_hello(name):
#     """
#     Priima varda ir atspausdina
#     :param name: zmogaus vardas
#     :return:
#     """
#
#     print(f'Hello, {name}')
#
# say_hello('Lopnu')
# print()


# def add(x: int, y: int) -> int:     #IMPORTANT!!!!
#     return x + y
# add(1, 3)


















