class Doctor:
    def feature1(self):
        print('feature1 is working')
    def feature2(self):
        print('feature2 is working')

class Doctor1(Doctor):
    def feature3(self):
        print('feature3 is working')
    def feature4(self):
        print('feature4 is working')

doc = Doctor1()
doc.feature1()
doc.feature2()
doc.feature3()
doc.feature4()