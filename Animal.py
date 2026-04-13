class Dog:
    def speak(self):
        print("Dog Barks")

class Cat:
    def speak(self):
        print("Cat Meows")

class Lion:
    def speak(self):
        print("Lion roar")


class Animal:
    def makesound(self,name):
        name.speak()


d=Dog()
c=Cat()
l=Lion()

a=Animal()
a.makesound(d)
a.makesound(c)
a.makesound(l)
