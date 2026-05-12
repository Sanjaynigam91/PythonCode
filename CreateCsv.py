import pandas as pd

Employee={'Name':['Sanjay','Rahul','Amit','Ajay','Ravi'],'Department':['IT','Sales','Marketing','Transport','Accounts'],
          'Salary':[100000,25000,20000,200000,15000]}
result=pd.DataFrame(Employee)
print(result)


result['Company']=['TCS','Infosys','HCL','Aj logistics','Adobe']
print(result)

result.to_csv('EmpCmp.csv',index=False)