import pandas as pd

data1=pd.DataFrame({"StateId":[1,2,3,4,5],"State":['UP','MP','Maharastra','Bihar','TamilNadu'],
                   "Capital":['Lucknow','Bhopal','Mumbai','Patna','Chennai']})
data2=pd.DataFrame({"StateId":[1,2,3,4,6],"State1":['Jammu & Kasmir','Bengal','Kerla','Karnatka','Delhi'],
                   "Capital1":['Sri Nagar','Kolkata','Trivendram','Banglore','Delhi']})

print("Merge with How for left partition")
result = pd.merge(data1,data2,how ="left")
print(result)
print("Merge with How for right partition")
result1 = pd.merge(data1,data2,how ="right")
print(result1)
print("Merge with How for outer partition")
result2 = pd.merge(data1,data2,how ="outer")
print(result2)
print("Indicators to check which data is present")
result3 = pd.merge(data1,data2,how ="outer", indicator=True)
print(result3)
print("Work with left and right index if Columns are same,")
data3=pd.DataFrame({"StateId":[1,2,3,4,5],"State":['UP','MP','Maharastra','Bihar','TamilNadu'],
                   "Capital":['Lucknow','Bhopal','Mumbai','Patna','Chennai']})
data4=pd.DataFrame({"StateId":[1,2,3,4,6],"State":['Jammu & Kasmir','Bengal','Kerla','Karnatka','Delhi'],
                   "Capital":['Sri Nagar','Kolkata','Trivendram','Banglore','Delhi']})
print("Merge with left and right index if Columns are same")
result4 = pd.merge(data4,data3, left_index=True , right_index=True)
print(result4)
print("Suffixes to change the name")
result5 = pd.merge(data4,data3, left_index=True , right_index=True,suffixes=("s","s"))
print(result5)
