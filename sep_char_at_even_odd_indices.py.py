# WAP to seperate the character at even and odd indices 

a='python is simple language'
even1=[]
odd1=[]
even=0
odd=0

i=0
while i< len(a):
    if i%2==0:
        even1.append(a[i])
        even+=1
    else:
        odd1.append(a[i])
        odd+=1
    i+=1

print ('char at even indice:',even1)
print ('char at odd indice:',odd1)
print ('No of char at even indice:',even)
print ('No of char at even indice:',odd)