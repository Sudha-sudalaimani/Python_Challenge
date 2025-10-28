class factorial():
    def __init__(self,n):
        self.num=n
        self.fact=1
    def display(self):
        for i in range(1,self.num+1):
            self.fact=self.fact*i
        print(f"Factorial of Given number is:{self.fact}")
n=int(input("Enter a number to find factorial:"))
fact_orial=factorial(n)
fact_orial.display()
