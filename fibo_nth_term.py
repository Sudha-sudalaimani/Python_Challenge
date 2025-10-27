num=int(input("enter a number:"))
a,b=0,1
for i in range(num-1):
    a,b=b,a+b
print(f"{num} th fibonacci term is:",a)
