# simple car solution
command = ""
is_car_started = False
while True:
    command = input(">").lower()
    if command == "start":
        if is_car_started:
            print("car is already started")
        else:
            is_car_started = True
            print("Car started...")
    elif command == "stop":
        if not is_car_started:
            print("Car is already stopped..")
        else:
            is_car_started = False
            print("Car stopped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit""")
    elif command == "quit":
        break
    else:
        print("sorry, I don't understand")

##########################################################
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + "  "
print(output)

#############################################################

# EMOJI CONVERTER
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😁",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)


#################################################################

class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("john smith")
print(john.name)
john.talk()

#################################################################

import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll)
