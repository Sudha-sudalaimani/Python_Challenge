class sum_digits():
    def __init__(self,i):
        self.input1=i
        self.sum=0
      
    def display(self):
            rem=self.input1
            while rem>0:
              digit=rem%10
              self.sum+=digit
              rem//=10
            print(self.sum)
number=int(input("Enter Number:"))
ans=sum_digits(number)
ans.display()
