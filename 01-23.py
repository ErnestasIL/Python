# listas = ['sausis', 'vasaris', 'kovas', 'balandis', 'geguze', 'birzelis']
#
# for elem in listas:
#     if elem == 'balandis':
#         break
#     print(elem)
# print('---------')
# for elem in listas:
#     if elem == 'sausis':
#         continue
#     print(elem)

#!!!!!!!!!!!!!!!!!!!!!!!!!!

# for skaicius in range(1, 5):
#     if skaicius % 2 == 0:
#         print('lyginis')
#     else:print('Nelyginis')
#

# print('-------------')
#
# skaiciu_listas = [1, 2, 3, 4, 5]
# for skaicius in skaiciu_listas:
#     if skaicius % 2 == 0:
#         print(skaicius, 'Lyginis')
# else:print('Ciklas baigtas')


                                        #Task!!!!!!!!!!!

# numbers_list = [1, 3, 5, 7, 8, 10, 11]
#
# for number in numbers_list:
#     if not number % 2:
#         print(number)
#         break
# else:print('no even number found')

                                        #comprehensions




# duomenu_listas = [1,10, 2, 20, 3, 30, 4, 40]

# for elem in duomenu_listas:
#     kaupiklis.append(elem)

# kaupiklis = [elem for elem in duomenu_listas]  #list comprehension

# print(kaupiklis)

# kaupiklis3 = [elem * 9 for elem in duomenu_listas]
# print(kaupiklis3)
#
# kaupiklis4 = [elem ** 2 for elem in duomenu_listas]
# print(kaupiklis4)
# print(duomenu_listas)

                                                #task

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# doubled = [elem * 2 for elem in numbers_list]
# print(doubled)
# squared = [elem ** 2 for elem in numbers_list]
# print(squared)
#
# euros = [10, 15, 20, 25, 30]
#
# dollars = [round(elem * 1.1, 1)  for elem in euros]
# print(dollars)
#
# kaina = [f'Kaina: {elem} EUR' for elem in euros]
# print(kaina)



#-------------------------------


# duomenu_listas = [1,10, 2, 20, 3, 30, 4, 40]
#
# kaupiklis = [[elem, elem ** 2] for elem in duomenu_listas]
# print(kaupiklis)
#
# kaupiklis1 = [[elem, elem ** 2, elem ** 2] for elem in duomenu_listas]
# print(kaupiklis1)


# listas = [1, 10, 2, 20, 3, 30, 4, 40, 99]
#
# k = [elem for elem in listas if elem < 10]
# print(k)


#-------------------- task!!!!


# numbers = [1, 2, 3, 4, 5]
#
# more_numbers = [[elem, elem ** 2, elem ** 3, elem % 2 == 0] for elem in numbers]
# print(more_numbers)
#
# credit_score = [5, 8, 12, 18, 25, 30, 35, 40]
#
# good_credit_score = [score for score in credit_score if score > 20]
# print(good_credit_score)
#
# round_credit_score = [score for score in credit_score if not score % 5]
# print(round_credit_score)
#
# odd_even_credit_score = [f'Even number: {score}' if not score % 2 else f'Odd number: {score}' for score in credit_score]
# print(odd_even_credit_score)
#
#
                                                #-----------------------

#
# raides = ['A', 'B', 'C']
# skaiciai = ['1', '2', '3', '4']
#
# raides_su_skaiciais = [raid + sk for raid in raides for sk in skaiciai]
# print(raides_su_skaiciais)
#

                                                #----------------------------

#
# listas = [0, 0, 5, 2, 3, 3, 3]
# print(set(listas))
#
#
#
# # tuple comprehension
# tuple_res = tuple(elem for elem in listas)
# print(tuple_res)  # (0, 0, 5, 2, 3, 3, 3)
#
# # dict comprehension
# dict_res = {elem: elem ** 2 for elem in listas}
# print(dict_res)  # {0: 0, 5: 25, 2: 4, 3: 9}
#
# # set comprehension
# set_res = {elem for elem in listas}
# set_res.add(4) # Gerai zinot nepagal tema !
# print(set_res)  # {0, 2, 3, 5}

                                                #---------Task!-------

letters = ['A', 'B', 'C']
numbers = [1, 2, 3]

added_numbers_with_letters = [lett + str(numb) for lett in letters for numb in numbers ]
print(added_numbers_with_letters)
index_numbers_letters = [lett + str(numb) for lett in letters for numb in numbers if letters.index(lett) + numb > 3]
print(index_numbers_letters)

numbers_letters_more = [lett.lower() + str(numb) for lett in letters for numb in numbers if not numb % 2]
print(numbers_letters_more)


sarasas = [1, 2, 3, 2, 1, 4, 5, 5]

set_sarasas = {elem for elem in sarasas}
print(set_sarasas)

tuple_sarasas = tuple(elem + 1 for elem in sarasas)
print(tuple_sarasas)

dict_sarasas = {elem: elem ** 2 for elem in sarasas}
print(dict_sarasas)



























