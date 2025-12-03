str=input('Enter String:')
vowels="aeiouAEIOU"
count=0
for ch in str:
    if ch in vowels:
        count+=1
print("Number of vowels in given String is:",count)
