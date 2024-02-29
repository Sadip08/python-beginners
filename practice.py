# Create a list
lst = [1, 2, 3]

# Reverse the list using the `reversed` function
reversed_lst = reversed(lst)

# Print the reversed elements one by one using the `next` function
print(next(reversed_lst))
print(next(reversed_lst))
print(next(reversed_lst))

# Attempting to print the next element will raise a StopIteration exception
print(next(reversed_lst)) # Exception

