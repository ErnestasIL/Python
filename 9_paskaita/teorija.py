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

name = 'Er'

def create_greetings(user):
    if not user:
        return
    res = f'greetings, {user}'
    return res

greetings = create_greetings(name)

if greetings:
    print(greetings)
else:print('No user! oh no')



