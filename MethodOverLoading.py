class OverLoading:

     def totalsum(self,a=None,b=None,c=None):
         r=0

         if a!=None and b!=None and c!=None:
             r=a+b+c
         elif a!=None and b!=None:
             r=a+b
         else:
             r=a
         return r


s1=OverLoading()
sum=s1.totalsum(1,2,6)
print(sum)