# WAP to fetch mobile no from string
a='my mobile no is 9090090900'

for i in a.split():
    if i.isdigit():
        print(i)

# WAP to do addition of digits of mobile number available in string
add=0
for i in a:
    if i.isdigit():
        add=add + int(i)
print(add)


# WAP to fetch vowels from string
for i in a:
    if i in 'aeiouAEIOU':
        print(i)