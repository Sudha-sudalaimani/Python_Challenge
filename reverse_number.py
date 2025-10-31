class reverse_number():
    def __init__(self,n):
        self.num=n
        self.rev=0
    def display(self):
        temp=self.num
        while temp!=0:
            digit=temp%10
            self.rev=self.rev*10+digit
            temp//=10
        print(self.rev)
n=int(input("Enter a Number:"))
reverse=reverse_number(n)
reverse.display()
