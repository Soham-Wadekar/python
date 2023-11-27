class Animal:

    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal

    def about_me(self):
        print(f"My name is {self.name} and I am {self.age} years old and I am {self.animal.lower()}.")

    def speak(self):
        print("'I don't know what to speak'")

class Cat(Animal):

    def __init__(self, name, age, animal, color):
        super().__init__(name, age, animal)
        self.color = color

    def speak(self):            
        print("'Meow'")

    def about_me(self):
        print(f"My name is {self.name} and I am {self.age} years old and I am {self.animal.lower()} and I'm {self.color.lower()} colored.")

class Dog(Animal):

    def speak(self):
        print("'Bark'")

class Fish(Animal):
    pass

p = Animal("Jumbo", 29, "Elephant")
p.about_me()
p.speak()

c = Cat("Simba", 12, "Cat","Ginger")
c.about_me()
c.speak()

d = Dog("Tommy", 7, "Dog")
d.about_me()
d.speak()

f = Fish("Nemo", 4, "Fish")
f.about_me()
f.speak()