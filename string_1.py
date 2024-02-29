# course = 'Python for beginners'
# print(len(course))
# course.upper()
# print(course.upper())
# print(course.lower())
# print(course.find('n'))
# print(course.replace('beginners', 'Absolute Beginners'))
# print('python' in course)
# print(course.title())
#
# # String slicing
# # done by slicing operator (:)
# print(course[3:12])
# print(course[3:-2])
# print(course[:-1])  # prints from index 0 to second last of the string
#
# # Reversing a string
# print(course[::-1]) # Reverses The String from beginning to second last elements
# reverse_course = "".join(reversed(course))
#
# # STRING FORMATTING
# #Accessing string from a Dictionary
# person= {'name': 'Jenn', 'age' : 34}
# sentence = 'My name is {} and  I am {} years old.'.format(person['name'],person['age'])
# sentence1 = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
# print(sentence)
# print(sentence1)
#
# my_name = 'Sadip'
# Her_name = "Sania"
# print('Hello I am {0} and She is {1}. Also He is {0}'.format(my_name,Her_name))

# class Person():
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# p1 = Person('Jack','33')
#
# sentence2 = 'My name is {0.name} and I am {0.age} years old'.format(p1)
# print(sentence2)

# sentence3 = 'My name: {name} and My age: {age}'.format(name= 'Jenn',age = '20')
# print(sentence3)

# print('Name : {name} and Age: {age}'.format(**person))

# for i in range(1,11):
#     sentence3 = 'The value is {:02}'.format(i) #displays two digit values
#     print(sentence3)

# pi = 3.14159265
# sentence4 = 'pi = {:.3f}'.format(pi) # displays three decimal values
# print(sentence4)

# print('1 MB  = {:,} bytes'.format(1000**2)) # separates the output using comma separator