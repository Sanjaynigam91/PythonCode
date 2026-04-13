class ExceptionHandling:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def divideNumber(self):
       print("start division of a number")
       try:
            c=self.a/self.b
            print(c)
       except ZeroDivisionError as e:
           print("Hey, You can't divide by zero a number",e)
       except Exception as e:
           print("Something went wrong, Please try again")
       finally:
           print("end division of a number")

def main():
    print("start main method execution")
    try:
        num = int(input("Enter a number"))
        num1 = int(input("Enter another number"))
        a1 = ExceptionHandling(num, num1)
        a1.divideNumber()
    except ValueError as e:
        print("Invalid Input",e)
    except Exception as e:
        print("Something went wrong, Please try again")
    finally:
        print("end main method execution")

if __name__ == "__main__":
    main()
