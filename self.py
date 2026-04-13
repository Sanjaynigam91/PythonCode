class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

    def compare(self,other):
        if self.age==other.age:
            print('Age is same')
        else:
            print('Age is different')

name1=input("Enter your name:").strip()
age1=int(input("Enter your age:"))

p=Person(name1,age1)
p.display()
name="Ajay"
age=30
p1=Person(name1,age1)
p1.display()

p.compare(p1)
