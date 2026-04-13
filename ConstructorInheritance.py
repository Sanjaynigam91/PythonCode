class A:
    def __init__(self):
        print('in init A is working')

    def feature1(self):
        print('feature 1-A is working')

    def feature2(self):
        print('feature 2-A is working')


class B(A):
    def __init__(self):
        super().__init__()
        print('in init B is working')


    def feature3(self):
        print('feature 3-B is working')

    def feature4(self):
        print('feature 4-B is working')


a1=B()
