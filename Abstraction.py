from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Laptop process")

class Programmer(Computer):
    def process(self):
        print("Programmer process")




com1=Laptop()
com1.process()
com2=Programmer()
com2.process()