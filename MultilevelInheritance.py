class A:
    def feature1(self):
        print('feature1 is working')
    def feature2(self):
        print('feature2 is working')
class B(A):
    def feature3(self):
        print('feature3 is working')

    def feature4(self):
        print('feature4 is working')

class C(B):
    def feature5(self):
        print('feature 5 is working')

c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()