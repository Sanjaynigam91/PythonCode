
class EmployeeData:
    def __init__(self,first,last,email):
        self.first = first
        self.last = last
        self.email = email
        self.dept=self.Department()

    def display(self):
            print(f'First Name: {self.first}')
            print(f'Last Name: {self.last}')
            print(f'Email: {self.email}')
            self.dept.display()

    class Department:
        def __init__(self):
            self.department = 'IT'
            self.DepartmentID = '101'

        def display(self):
            print(f'Department ID: {self.DepartmentID}')
            print(f'Department Name: {self.department}')



d1=EmployeeData('arpit','Shukla',"arpit@gmail.com")
d1.display()
d2=EmployeeData('Sanjay','Nigam','sanjay@gmail.com')
d2.display()