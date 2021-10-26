
def countdown(input_number):
    new_list = []
    for x in range(input_number, -1,-1):
        new_list.append(x)
    return new_list

print(countdown(4))


def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))


def values_greater_than_second(list):
    new_list = []
    if len(list) < 2:
        return False
    for x in list:
        if x > list[1]:
            new_list.append(x)
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))


def first_plus_length(list):
    val1 = list[0] + len(list)
    return val1

print(first_plus_length([1,2,3,4,5]))


def length_and_value(size,value):
    list = []
    for x in range(0,size):
        list.append(value)
    return list

print(length_and_value(5, 4))