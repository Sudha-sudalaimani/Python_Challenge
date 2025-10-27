#armstrong Number
num=153
x=num
sum=0
while num>0:
    digit=num%10
    sum+=digit**3
    num//=10
if (sum==x):
    print(x,"Armstrong Number")

else:
    print(x,"Not a Armstrong Number")
