#list: ordred, mutable, allows duplicate elements

mylist = ['banana', 'cherry', 'apple']
print(mylist)

mylist2 = list()
print(mylist2)
#can append later

mylist2 = [5, True, 'apple', 'apple']
print(mylist2)

item = mylist[0]  # the first item at index 0
print(item)
item2 = mylist[-1] # assigns to the last item in the list


mylist = ['banana', 'cherry', 'apple']

for i in mylist:
    print(i)


#to check an item inside a list
if 'banana' in mylist:
    print('yes')

else:
    print('No')

print(len(mylist))

mylist.append('lemon')

print(mylist)

# to insert an iitem at a specific position

mylist.insert(1, 'blueberry')

# to emove items

item = mylist.pop() # returns the last item and also removes it
print(item)
print(mylist)


# remove method
mylist.remove('blueberry')

# to remove all elements
item = mylist.clear()

# to reverse the list
item = mylist.reverse()
# to sortyour list

item = mylist.sort()

# to create a new list, not altering the original
new_list = sorted(mylist)
print(mylist)
print(new_list)

#concat a list
mylist = [0]*5
print(mylist)

mylist2 = [1,2,3,4,5]

new_list1 = mylist + mylist2
print(new_list1)

mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5]

a = mylist[1:5]
#step method
b = mylist[1::2]

print(b, 'step method')

#copying a list
list_org = ['banana', 'cherry', 'apple']

list_cpy = list_org.copy()  # list_org[:] list(list_org)  also makes actual copies

list_cpy.append('lemon')

print(list_cpy)
print(list_org)

#list comprehension
a = [1,2,3,4,5,6]
b = [i*i for i in mylist]

print(mylist)
print(b)



