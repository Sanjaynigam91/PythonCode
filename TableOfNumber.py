class TableOfNumber:
    def __init__(self,number):
        self.number = number

    def process(self):
        for i in range(1,11):
            print(self.number*i)

n=int(input("Enter a number"))
values = TableOfNumber(n)

values.process()