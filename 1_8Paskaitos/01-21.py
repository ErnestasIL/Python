#Round ir Sorted metodai

# x = 1.2154163546
#
# res = round(x, 2)  #Apvalina nuo 5 zemyn nuo 6 aukstyn
# print(res)


# import locale
# locale.setlocale(locale.LC_ALL, 'lt_LT')
# list_lt = ["Žemė", "Ąžuolas", "Vilnius"]
# res = sorted(list_lt, key=locale.strxfrm)
# print(res)  # ['Ąžuolas', 'Vilnius', 'Žemė']

                                                    #Task!!!

# numbers = [1.234, 3.14159, 2.71828, 0.57721]
# rounded_numbers = []
# for number in numbers:
#      rounded_numbers.append(round(number, 3))
# print(rounded_numbers)
#
#
# import locale
# locale.setlocale(locale.LC_ALL, 'lt_LT')
# words = ['Žalgiris', 'Ąžuolas', 'Vilnius', 'Lietuva']
# results = sorted(words, key=locale.strxfrm)
# print(results)
#
# numbers_duo = [10, 3, 7, 1, 15]
# print(sorted(numbers_duo, reverse= True))

                                            #duomenu struktuos ZODYNAI

# person_info = {
#     'name': 'Albert',
#     'surname': 'Einstein',
#     'languages': ['German', 'Latin', 'Italian', 'Engish'],
#     'occupation': {
#         'role': 'Professor',
#         'workplace': 'University of Berlin'
#     }
# }
# for key, value in person_info.items():
#     # print(f'key: {key} value: {value}')
#     if type(value) == dict:
#         for k, val in value.items():
#             print(f'Key: {k} value: {val}')
# # print(person_info['name'])
# # print(person_info['languages'][0])
# # print(person_info['languages'][2])
# # print(person_info['occupation']['role'])
# # print(person_info['occupation']['workplace'])
# # print(person_info)
# # print(type(person_info))

                                                #Task!!!!

school = {
    'name': 'School of Python',
    'teachers': {
        'teacher1': {
            'name': 'John',
            'surname': 'Smith',
            'teaches': 'Math'
        },
        'teacher2': {
            'name': 'Bella',
            'surname': 'Simons',
            'teaches': 'Geography'
        },
        'teacher3': {
            'name': 'Chris',
            'surname': 'Brown',
            'teaches': 'English'
        },
        'teacher4': {
            'name': 'Barbara',
            'surname': 'Strizen',
            'teaches': 'Arts'
        }


    },
    'no_of_students': 456
}
# print('teachers name is: ' + school['teachers']['teacher1']['name'])
# print('teaches: ' + school['teachers']['teacher1']['teaches'])
#
# if school['no_of_students'] > 500:
#     print('More than 500 students')
# else:print('Less than 500 students')

company = {
    'name': 'TechCorp',
    'employees': [{
        'name': 'Jonas',
        'role': 'Developer',
        'salary': 3000
    },
    {
        'name': 'Asta',
        'role': 'Designer',
        'salary': 2500
    },
    {
        'name': 'Tomas',
        'role': 'Manager',
        'salary': 4000
    }],
    'location': 'Vilnius',
    'industry': 'IT'
}
# for emplo in company['employees']:
#     print(emplo['name'], emplo['role'])
# total_sum = sum(emplo['salary'] for emplo in company['employees'])
# print(total_sum)
# average_salary = total_sum /len(company['employees'])
# print(round(average_salary, 3))

if 'location' in company:
    print('yes')
else:print('No')

print(company.get('location'))


library = { "books": [
    {"title": "1984",
     "author": "George Orwell",
     "copies": 3},
     {"title": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "copies": 5},
    {"title": "The Great Gatsby",
     "author": "F. Scott Fitzgerald",
     "copies": 2} ],
    "location": "Kaunas",
    "open_hours": {
        "start": "8:00", "end": "20:00"} }

# for book in library['books']:
#     print(f'Book title is: {book["title"]}, and Author is: {book["author"]} ')

min_copies_of_books = library['books'][0]

for book in library['books']:
    if book['copies'] < min_copies_of_books['copies']:
        min_copies_of_books = book
print(min_copies_of_books['title'])