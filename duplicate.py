# WAP to separate duplicate item from list
l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
a=0
'''
while a < len(l):
    for i in l:
        if i not in l1:
            l1.append(i)
        else:
            print(i,end=' ')
        a=a+1


for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')
'''

unique=[]
dup=[]
for i in l:
    if l.count(i)==1:
        unique.append(i)
    else:
        dup.append(i)
print(dup)
print(unique)
