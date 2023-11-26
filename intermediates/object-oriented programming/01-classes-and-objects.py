# Class - A blueprint of the object
# Object - An instance of the class

class Dog:                  # Class

    def bark(self):         # Class Method
        print("BARK!...Method Called")


animal = Dog()              # Object (Instance of class Dog)

print(f"The type of the instance 'animal' is {type(animal)}")
print(f"Calling a method:")
animal.bark()