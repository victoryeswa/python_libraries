#dictionary:Key-Value pairs, unordered, Mutable
mydict = {'name': 'Max', 'age': 28, 'city':"New York"}
print(mydict)

mydict2 = dict(name='Mary', age=27, city='Boston')

print(mydict2)

#to access values
value = mydict['name']
print(value)

#checking a dict value that is unavailable will raise a keyerro

#adding a value to a dictionary

mydict['email'] = 'victoryeswa.com'
print(mydict)

#deleting a value 
del mydict['name']
print(mydict)

#also
mydict.pop('age')  # mydict.popitem() --removes the last inserted item

#to chck for items

if 'name' in mydict:
    print(mydict['name'])


try:
    print(mydict['name'])
except:
    print('Error')

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)


#copyinng a dictionary

mydict_cpy = mydict.copy()

mydict_cpy['email'] = 'congestina.com'
print(mydict_cpy)
print(mydict)

#the update method

mydict = {'name':'Max', 'age':28, 'email':'max.com'}
mydict2 = dict(name='mary', age=27, city='boston')

mydict.update(mydict2)

print(mydict)

#using a tuple in a dictionary
mytupe = (5,7)
mydict = {mytupe, 12}

print(mydict)




































