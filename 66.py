um=int(input())
if(um>1):
   for i in range(2,um):
      if(um%i)==0:
         print("no")
         break
   else:
         print("yes")
 
else:
   print("no")
