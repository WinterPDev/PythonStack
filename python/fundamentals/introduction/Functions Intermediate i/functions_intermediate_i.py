x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30

print(x[1][0])
print(students[0]["last_name"])
print(sports_directory["soccer"][0])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(some_list):
#     for i in range(len(some_list)):
#         for key, value in some_list[i].items():
#             print(f"{key} - {value}")
#     return some_list

# iterateDictionary(students)


# def iterateDictionary2(key_name,some_list):
#     for i in range(len(some_list)):
#         print(some_list[i][key_name])
#     return some_list

# iterateDictionary2("first_name",students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def print_info(some_dict):
    for i in some_dict:
        print(str(len(some_dict[i]))+ str(list(some_dict.keys())[0]))
        print(some_dict[i])
    return some_dict


print_info(dojo)