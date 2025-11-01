class check_palindrome():
    def __init__(self,t):
        self.text=t
        self.rev=""
    def display(self):
        res=self.text
        for i in res:
            self.rev=i+self.rev
        if res==self.rev:
            print("Palindrome")
        else:
            print("Not a Palindrome")

t=input('Enter a word:')
cp=check_palindrome(t)
cp.display()
