num1 = 42 # variable declaration Numbers
num2 = 2.3 # variable declaration Numbers
boolean = True # variable declaration Boolean
string = 'Hello World' # variable declaration string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, List
print(type(fruit)) # log statement, type check, list access value
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') # List add value
print(person['name']) # log statement, Dictionary access Value
person['name'] = 'George' # Dictionary, change value
person['eye_color'] = 'blue' # Dictionary, change value
print(fruit[2]) # log statement

if num1 > 45: # conditional if
    print("It's greater") # log statement
else:   
    print("It's lower") # log statement

if len(string) < 5:             # length check, conditional if
    print("It's a short word!") # log statement
elif len(string) > 15:          # length check, else if
    print("It's a long word!") # log statement
else:                          # else 
    print("Just right!") # log statement,

for x in range(5): # for loop start
    print(x) # log statement
for x in range(2,5): # for loop start
    print(x) # log statement
for x in range(2,10,3): # for loop start
    print(x) # log statement
x = 0        # variable declaration, change value
while(x < 5): # while loop start
    print(x) # log statement
    x += 1   # change value, increment

pizza_toppings.pop() # list, delete value
pizza_toppings.pop(1) # list, delete value, access value

print(person) # log statement
person.pop('eye_color') # Dictionary, delete value
print(person) # log statement

for topping in pizza_toppings:  # for loop start
    if topping == 'Pepperoni': # conditional if
        continue               # for loop
    print('After 1st if statement') # log statement
    if topping == 'Olives':   # conditional if
        break

def print_hello_ten_times(): # function ( parameter) 
    for num in range(10):    # for loop start
        print('Hello') # log statement

print_hello_ten_times() # log statement

def print_hello_x_times(x): # function ( parameter)
    for num in range(x):   # for loop start
        print('Hello') # log statement 

print_hello_x_times(4) # log statement

def print_hello_x_or_ten_times(x = 10): # function ( parameter)
    for num in range(x):  # for loop start
        print('Hello') # log statement

print_hello_x_or_ten_times() # log statement
print_hello_x_or_ten_times(4) # log statement

# comment multiline v
"""
Bonus section
"""

# print(num3) # log statement
# num3 = 72
# fruit[0] = 'cranberry', List
# print(person['favorite_team']) # log statement, List
# print(pizza_toppings[7]) # log statement, List
#   print(boolean) # log statement
# fruit.append('raspberry')
# fruit.pop(1)