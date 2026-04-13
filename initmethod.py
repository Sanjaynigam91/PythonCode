class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        print(c)
    def mul(self):
        c=self.a* self.b
        print(c)


x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
t1=Test(x,y)
t1.add()
t1.mul()



