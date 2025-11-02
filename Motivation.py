class Motivation():
    def __init__(self,q):
        self.quote=q
    def display(self):
        msg=self.quote
        print(msg)
q=input("Enter Quote To Display:")
motivation=Motivation(q)
motivation.display()
