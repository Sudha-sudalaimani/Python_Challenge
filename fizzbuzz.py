class fizzbuzz():
    def __init__(self,s,e):
        self.start=s
        self.end=e
    def display(self):
        for i in range(self.start,self.end+1):
            if(i%3==0 and i%5==0):
                print("FizzBuzz")
            elif(i%3==0):
                print("Fizz")
            elif(i%5==0):
                print("Buzz")
            else:
                print(i)
start=int(input("Enter number:"))
stop=int(input("Enter a Number:"))
fb=fizzbuzz(start,stop)
fb.display()
