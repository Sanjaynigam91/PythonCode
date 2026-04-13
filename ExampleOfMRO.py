class A:
    def __init__(self):
        print('in init A')
    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')

class B:
    def __init__(self):
        print('in init B')
    def feature3(self):
        print('feature 3 is working')
    def feature4(self):
        print('feature 4 is working')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('in init C')
    def feature5(self):
        print('feature 5 is working')
    def feature6(self):
        print('feature 6 is working')

    def feat(self):
        super().feature1()
        super().feature2()

c1=C()
c1.feat()
