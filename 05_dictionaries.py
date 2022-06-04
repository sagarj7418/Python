d=dict()
d.update({1:100,2:200,3:300}) # update the dictionary
x=d.copy()    # create shallow copy of dict.
print(id(x))
print(id(d))
#print(d.keys())      #it gives list of dictionary keys
#print(d.get(1))       # it gives value of specified key
#print(d.values())      # it gives list of all values in the dict.
#print(d.items())        # it gives list contains tuple of each key-value pair
'''
s=['x','y','z']
r=(1)
print(dict.fromkeys(s,r))  # Create a new dictionary with keys from iterable and values set to value.
'''
#d.pop(1)      # it removes the key-value pair of specified key
#d.popitem()    # it removes the last key-value pair

#print(d.setdefault(4,400))  # it will returns value of specified pair ,if not exist then insert given kay-value pair
print(d)
d.clear()       # it delete all items from dictionary.
print(d)