# import function
# print(function.emoji_converter("I am happy :("))
#
# ####################################################
# from function import emoji_converter
# print(emoji_converter("I am happy :)"))
#
# ####################################################
def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max
