num=int(input("Enter a number:"))
if num>0:
    for i in range(2,int(num**0.5)):
        if num%i==0:
            print(num,"Not a prime number")
            break
    else:
        print(num,"Prime number")
else:
    print("Number Must Be Greater Than 1")
