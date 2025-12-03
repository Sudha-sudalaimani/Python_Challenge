#Write a Python function that takes a list of integers and returns a new list containing only the even numbers.
#[1, 2, 3, 4, 5, 6] input sample
#[2, 4, 6] output sample

lst=[1,2,3,4,5,6]
even_numbers=[]
for i in lst:
    if i%2==0:
        even_numbers.append(i)
print(even_numbers)
