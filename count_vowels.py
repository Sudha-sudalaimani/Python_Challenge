class count_vowels():
    def __init__(self,w):
        self.vowels="aeiouAEIOU"
        self.count=0
        self.word=w
    def display(self):
        temp=self.vowels
        total=self.count
        word1=self.word
        for i in word1:
            if i in temp:
                total+=1
        print("No of vowels:",total)
cv=count_vowels("Hello world")
cv.display()
