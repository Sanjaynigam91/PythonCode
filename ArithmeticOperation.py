import pandas as pd

data=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10]})
print(data)

#Addition
data['Add']=data['a']+data['b']
print(data)

#Substraction
data['Sub']=data['b']-data['a']
print(data)

#Multiplication
data['Multiply']=data['a']*data['b']
print(data)

#Division
data['Divide']=data['b']/data['a']
print(data)

#Reminder
data['Reminder']=data['b']%data['a']
print(data)

#Check Number which is less or equal to 10 in Add
data['Number']=data['Add']<=10
print(data)

#Check Even
data['Even'] = data['b'] % 2 == 0
print(data)

def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False

data['Prime'] = data['Add'].apply(isPrime)

print(data)
