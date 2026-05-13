import pandas as pd
csv_file = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_50_records_missing_data.csv")
print(csv_file)

#print(csv_file.dropna())
#print(csv_file.dropna(how="any"))
#print(csv_file.dropna(inplace=True))
#print(csv_file.dropna(thresh=1))

#print(csv_file.fillna("Sanjay"))
#res=csv_file.fillna({"EmployeeID":"EmpId","Name":"Sanjay","Age":18,"Salary":10000})
#print(res)

res1 = csv_file.bfill()
print(res1)