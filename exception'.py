try:
    age = int(input('Age = '))
    income = 20_000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid value')
