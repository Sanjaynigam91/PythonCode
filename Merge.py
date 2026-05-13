import pandas as pd

data1=pd.DataFrame({"StateId":[1,2,3,4,5],"State":['UP','MP','Maharastra','Bihar','TamilNadu'],
                   "Capital":['Lucknow','Bhopal','Mumbai','Patna','Chennai']})
data2=pd.DataFrame({"StateId":[1,2,3,4,5],"State1":['Jammu & Kasmir','Bengal','Kerla','Karnatka','Delhi'],
                   "Capital1":['Sri Nagar','Kolkata','Trivendram','Banglore','Delhi']})

result = pd.merge(data1,data2,on="StateId")
print(result)
