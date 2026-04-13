from zipapp import create_archive


class Car:
    wheels=4
    def __init__(self):
        self.color = "White-Black"
        self.company="Defender"


c1=Car()
c1.color = "White-Gray"
c2=Car()

Car.wheels=5

print(c1.color,c1.company,c1.wheels)
print(c2.color,c2.company,c2.wheels)



