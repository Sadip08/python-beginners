# try:
#     f = open('testfile.txt', 'r')
#     var = bad_var
# except FileNotFoundError:
#     print("Sorry. This file doesnot exist")
# except Exception:
#     print("something went wrong")
#
# try:
#     f = open('testfile.txt', 'r')
#     var = bad_var
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
#
try:
    f = open('test1.txt')
    if f.name == "test1.txt":
        raise Exception
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally")


