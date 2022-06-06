a='i am going to purchase items with price 40,50,60'
print(a.split(','))
print(int(a.split(',')[-1]))


add=0
for i in a.split(','):
    add+= int(i.split()[-1])

print(add)