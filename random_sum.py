import random
random_num=[random.randint(1,100) for i in range(10)]
total=0
for x in random_num:
    total+=x
print(total)
