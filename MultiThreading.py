from time import sleep
from threading import *

class GoodMorning(Thread):
    def run (self):
        for i in range(10):
            print("Good Morning")
            sleep(1)


class GoodEvening(Thread):
    def run (self):
        for i in range(10):
            print("Good Evening")
            sleep(1)

g1 = GoodMorning()
e1=GoodEvening()
g1.start()
sleep(0.5)
e1.start()

g1.join()
e1.join()
print("Bye,Good Night")
