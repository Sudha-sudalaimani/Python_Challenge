class student():
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
s1=student("Sam",100)
s2=student("Thashlee",100)
s3=student("Ram",100)
s1.display()
s2.display()
s3.display()
    
