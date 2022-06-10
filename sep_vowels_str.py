# WAP to seperate Vowels from string and prints count
a='I am Data Scientist'
x=[]
add=0
for i in a:
    if i in 'aeiouAEIOU':
        print(i,end='')
        x.append(i)
        add+=1
print('\n',add)