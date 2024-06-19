a=int(input("A:"))
b=int(input("B:"))
operation=input("add/sub/mul/div:")
if(operation=="add"):
   print(a+b)
elif(operation=="sub"):
   print(a-b)
elif(operation=="mul"):
   print(a*b)
elif(operation=="div"):
   print(a/b)
else:
   print("invalid operator")

#A:10
#B:20
#add/sub/mul/div:add
#30
