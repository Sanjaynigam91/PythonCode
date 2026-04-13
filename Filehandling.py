
f=open('Mydata','r')

print(f.read())

f1=open('xyz','w')

for data in f:
    f1.write(data)

f2=open('photo.png','rb')

f3=open('MyPhoto.jpg','wb')
for pdata in f2:
    f3.write(pdata)


