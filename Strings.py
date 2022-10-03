# Vars
# myStr = "This is my string."
firstString = "water"
secondString = "fall"
myStr = firstString + secondString
name = None
color = None
animal = None

# Code
print(myStr)
print(type(myStr))
print(str(myStr) + " is my val and is of type " + str(type(myStr)))
name = input("Enter your name: ")
color = input("Enter your fav color: ")
animal = input("Enter your fav animal: ")

print("{}: Fav color: {} & fav animal: {}".format(name, color, animal))