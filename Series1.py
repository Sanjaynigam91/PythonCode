from operator import index

import pandas as pd

datalist={"City":['Lucknow','Mumbai','Bhopal','Kolkata','Bangalore'],"States":['UP','Maharashtra','MP','Bengal','Karnataka'],
          "Rank":[1,2,3,4,5]}

result=pd.Series(datalist)
print(result)
print(result['Rank'])
print(type(result))
