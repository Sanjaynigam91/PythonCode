from dbm import sqlite3


class StudentMarks:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=StudentMarks(m1,m2)
        return m3

    def __sub__(self,other):
        m1=self.m1-other.m1
        m2=self.m2-other.m2
        m3=StudentMarks(m1,m2)
        return m3

    def __str__(self):
        return f"{self.m1},{self.m2}"



s1=StudentMarks(10,20)
s2=StudentMarks(20,30)
s3=s1+s2
s4=s1-s2
print(s3)
print(s4)



