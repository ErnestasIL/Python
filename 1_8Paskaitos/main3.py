#Create empty list

sarasas = []

# print(type(sarasas))
print(sarasas)

#Data to add to list
men1 = 'sausis'
men2 = 'vasaris'

#Use .append to add element to the end of the list
sarasas.append(men1)
print(sarasas)
sarasas.append(men2)
print(sarasas)

sarasas.append('kovas')
print(sarasas)

# .insert() add element to list by index

sarasas.insert(0, 'balandis')#must add index place
sarasas.insert(-1, 'balandis')
print(sarasas)

sarasas.insert(2, 'birzelis')
print(sarasas)

# indexes in list
print(sarasas[1])
print(sarasas[1 :])
print(sarasas[1 : 3])
print(sarasas[:: 2])

# .remove() used to remove first element from list by object

sarasas.remove('balandis')
print(sarasas)

# .pop() used to remove first element from list by object and index

sarasas.pop()
print(sarasas)
ismestas = sarasas.pop(1) #galima issaugot atskiram kintamajam
print(sarasas)
print(ismestas)

#del sarasas[-1]  istrina vapsie is pc nebegalesi naudot geriau naudot pop


#task 1

animals = ['Suo', 'kate', 'zuikis']
print(animals)
animals.append('dramblys')
print(animals)
animals.insert(1, 'zirafa')
print(animals)
animals.remove('kate')
print(animals)
lost_animal = animals.pop(-1)
print(lost_animal)
animals[0] = 'tigrai'
print(animals)