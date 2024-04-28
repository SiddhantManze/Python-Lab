import mymodule
from mymodule import person

name = input("Your name: ")

mymodule.greet(name)

print(mymodule.person["name"])