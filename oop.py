######################################
# CLASS
class Point:

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

point2 = Point(10, 20)
point2.x = 1
print(point2.x, point2.y)


# Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):

    def be_annoying(self):
        print("Annoying")


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.be_annoying()

#################################################################

class Person:

    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("john smith")
print(john.name)
john.talk()

#################################################################
