# # Create a list
# lst = [1, 2, 3]
#
# # Reverse the list using the `reversed` function
# reversed_lst = reversed(lst)
#
# # Print the reversed elements one by one using the `next` function
# print(next(reversed_lst))
# print(next(reversed_lst))
# print(next(reversed_lst))
#
# # Attempting to print the next element will raise a StopIteration exception
# print(next(reversed_lst)) # Exception

# import time
# import datetime
#
# #To get current GM time print("Current GM time:",time.gmtime()) #This returns a time structure containing 9 values
# - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.
#
# #To get current local time print("Current local time:",time.localtime()) #This also returns a time structure
# containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.
#
# #To extract today's date in a specified string format
# print("Today's date using time module",time.strftime("%m-%m/%Y"))
#
# #Python additionally allows use of  datetime module
# #Prints today's date
# print("Today's date using datetime module:", datetime.date.today())
#
# #To extract today's date in a specified string format
# print("Today's date (dd/mm/yyyy) using datetime module:", datetime.date.today().strftime("%d/%m/%Y"))
#
#
# #To convert a date in string format to datetime value
# print("Today's date (dd/mm/yyyy):", datetime.datetime.strptime("17/04/1","%y/%d/%m"))

# lex_auth_01269444195664691284

# lex_auth_01269444195664691284

# def encrypt_sentence(sentence):
#     words = sentence.split()
#     en = []
#     def rearrange(word):
#         vowels = 'aeiouAEIOU'
#         cons = ''.join([ch for ch in word and ch not in vowels])
#         vow = ''.join([ch for ch in word and ch in vowels])
#         return cons+vow
#     for i, word in enumerate(words):
#         if i + 1 %2 != 0 :
#             en.append(word[::-1])
#         else:
#             en.append(rearrange(word))
#     return ' '.join(en)
#     #start writing your code here
#
# sentence="The sun rises in the east"
# encrypted_sentence=encrypt_sentence(sentence)
# print(encrypted_sentence)
# sentence="The sun rises in the east"
# encrypted_sentence=encrypt_sentence(sentence)
# print(encrypted_sentence)

# def calculate_sum(list_of_expenditure):
#     total = 0
#     try:
#         for expenditure in list_of_expenditure:
#             total += expenditure
#         print("Total:", total)
#         avg = total / no_values
#         print("Average:", avg)
#     except ZeroDivisionError:
#         print("Divide by Zero error")
#     except TypeError:
#         print("Wrong data type")
#
#
# try:
#     list_of_values = [100, 200, 300, 400, 500]
#     num_values = len(list_of_values)
#     calculate_sum(list_of_values)
# except NameError:
#     print("Name error occured")
# except:
#     print("Some error occured")
# def find_average(mark_list):
#     total = 0

#     try:
#         for i in range(0, len(mark_list)):
#             total += mark_list1[i]
#             marks_avg = total / len(mark_list)
#             return marks_avg
#     except NameError:
#         print("Name Error")
#     except ValueError:
#         print("Value Error")
#     except:
#         print("Error")


# m_list = ["1", 2, 3, 4]
# print("Average marks:", find_average(m_list))


# def find_factors(num):
#     #Accepts a number and returns the list of all the factors of a given number
#     factors = []
#     for i in range(2,(num+1)):
#         if(num%i==0):
#             factors.append(i)
#     return factors

# def is_prime(num, i):
#     #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
#     if(i==1):
#         return True
#     elif(num%i==0):
#         return False
#     else:
#         return(is_prime(num,i-1))

# def find_largest_prime_factor(list_of_factors):
#     factors = list_of_factors.sort(reverse = True)
#     for i in factors:
#         if is_prime(i,i/2):
#             return i
#     #Accepts the list of factors and returns the largest prime factor

# def find_f(num):
#     factors = find_factors(num)
#     return find_largest_prime_factor(factors)
     
#     #Accepts the number and returns the largest prime factor of the number

# def find_g(num):
#     add = 0
#     for i in range(0,9):
#         add += find_f(num + i)
#     return add
#     #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number

# #Note: Invoke function(s) from other function(s), wherever applicable.

# print(find_g(10))

# def find_nine(nums):
#     if len(nums) < 4:
#         length = len(nums)
#     else:
#         length = 3
# 	i = 0
# 	while i <= length :
# 	   if nums[i] ==9:
# 	       return True
# 	   i+=1
#     return False
 
    
# nums=[1,9,4,5,6]
# print(find_nine(nums))

# def seed_no(number,ref_no):
#     temp = number
#     num = []
#     while temp > 0:
#         num.append(temp%10)
#         temp //= 10
#     for i in num:
#         number *= int(i)
#     return number == ref_no
#     #start writing your code here
    
# number=224
# ref_no=3582
# print(seed_no(number,ref_no))

# def check_prime(number):
#     if number <= 1:
#         return False
#     if number == 2:
#         return True  # 2 is prime
#     if number % 2 == 0:
#         return False  # other even numbers are not prime
    
#     # check odd factors up to square root of number
#     for i in range(3, int(number**0.5) + 1, 2):
#         if number % i == 0:
#             return False
#     return True

# def rotations(num):
#     str_num = str(num)
#     length = len(str_num)
#     rotation_list = []
#     for i in range(length):
#         rotated = str_num[i:] + str_num[:i]
#         rotation_list.append(int(rotated))
#     return rotation_list

# def get_circular_prime_count(limit):
#     count = 1
#     n =[]
#     for i in range(3, limit,2):
#         if all(check_prime(num) for num in rotations(i)):
#             count += 1
#             n.append(i)
#     return count,n

# print(get_circular_prime_count(1000))
