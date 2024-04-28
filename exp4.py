class Animal:
    name = ""

    def eat(self):
        print("I can eat")

class Dog(Animal):
    def display(self):
        print("My name is", self.name)

Pet = Dog()
Pet.name = "Rohu"
Pet.eat()
Pet.display()

