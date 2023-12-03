# Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines.

class Cat:

    def sound(self):
        print("Meow!")

class Dog:

    def sound(self):
        print("Bark!")

class Owl:

    def sound(self):
        print("Hoot!")

class AnimalSound:

    def speak(self, animal):
        animal.sound()


cat = Cat()
dog = Dog()
owl = Owl()

sound = AnimalSound()
sound.speak(cat)
sound.speak(dog)
sound.speak(owl)