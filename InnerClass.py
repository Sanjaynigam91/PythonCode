
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.car=self.Car()

    def display(self):
        print(self.name,self.age)
        self.car.display()

    class Car:
        def __init__(self):
            self.brand='CRETA'
            self.model='2024'
            self.mileage=10

        def display(self):
            print(self.brand,self.model,self.mileage)




e1=Employee('Sanjay',30)
e1.display()
e2=Employee('arpit',40)
e2.display()
