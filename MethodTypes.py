


class Students:
    schoolName="BBD University"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def get_average(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.schoolName

    @staticmethod
    def info():
        print("this is student from different university module")

s1=Students(50,60,70)
s2=Students(75,80,95)

print(s1.get_average())
print(s2.get_average())
stdResult=Students.getSchool()
print(stdResult)
Students.info()



