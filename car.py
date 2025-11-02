class car():
    def __init__(self,b,m,y):
        self.brand=b
        self.model=m
        self.year=y
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print('Year:',self.year)
audi=car("Audi","ZZ6t",2020)
audi.display()

bmw=car("BMW","YYw2",2021)
bmw.display()
