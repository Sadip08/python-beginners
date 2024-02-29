# numbers = [5, 3, 4, 2, 7, 10]
# print(numbers)
#
# numbers.insert(0, 10)  # (index, object to insert in the index)
# print(numbers)
#
# numbers.remove(5)  # removes specific items
# print(numbers)
#
# numbers.clear()  # removes all the items in the list
#
# numbers.pop()  # removes the value at the last index of the list
#
# numbers.index(5)  # returns the index of the parameter in the list
#
# print(5 in numbers)  # returns (BOOLEAN) the existence of the object in a list
#
# numbers.count(5)  # returns the count of the object's existence in the list
#
# numbers.sort()  # sorts elements in ascending order
# numbers.reverse()  # sorts elements in descending order
# print(numbers)
#
# numbers2 = numbers.copy()  # creates a copy of numbers in numbers2
#
# # WAP to remove duplicates in a list
#
# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)
#
import random


#
# # Sort list, tuples, Objects
# list = [9, 1, 8, 7, 4, 5, 6, 2, 3, 4]
# random.shuffle(list)
# print(list)
#
# s_list = sorted(list)  # returns sorted list to a new list without sorting the actual list
# print(s_list)
#
# s_rev_list = sorted(list, reverse=True)
# print(s_rev_list)
# list.sort(reverse=True)  # sorts the actual list
# print(list)

# Tuple
# Tuple does not have sort() method instead has sorted() method

# Dictionary
# dict = {n:n*n for n in range(0,10)}
# random.shuffle(dict)
# s_dict = sorted(dict)
# print(s_dict)

# Sorting based on a criteria
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Sadip', 27, 4000)
e2 = Employee('Madan', 23, 20000)
e3 = Employee('Mingmar', 27, 60000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort, reverse=False)
print(s_employees)
