#Factorial Range
start=int(input('enter a number:'))
end=int(input("Enter a number:"))
fact=1
for i in range(start,end+1):
    fact=fact*i
print(fact)
