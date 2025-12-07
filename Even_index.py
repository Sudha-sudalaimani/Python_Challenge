#One method
def even_index():
    str=input('Enter a string:')
    for i,word in enumerate(str):   #Pynative
        if i%2==0:                  #01234567
            print(word)
even_index()

#Another method
def index():
    words=input("Enter word")
    print(f"Original Word:{words}")
    size=len(words)
    for i in range(0,size-1,2):
        print(words[i])
index()
