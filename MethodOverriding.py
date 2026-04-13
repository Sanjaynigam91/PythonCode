class Overloading:
    def display(self):
        print("Working display in class A")


class Overloading1(Overloading):
   def display(self):
       print("Working display in class B")


a=Overloading1()
a.display()
