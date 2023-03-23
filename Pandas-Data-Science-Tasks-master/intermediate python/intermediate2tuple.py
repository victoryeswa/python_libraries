#tuple: ordered, imutable, allows duplicate elements

mytuple = ('Max', 28, 'Boston')
print(type(mytuple))

#built in tuple function
mytuple2 = tuple(['Max', 28, 'Boston'])
print(mytuple2)

item = mytuple2[0]
print(item)
# does not support item assignment - immutable

for i in mytuple2:
    print(i)

if 'Max' in mytuple2:
    print('Yes')
else:
    print('No')


mytuple = ('a','p','p','l','e')

print(mytuple.count('a')) #returns number of occurence of value

print(mytuple.index('p')) # gives the fist occurence

my_list = list(mytuple)

print(my_list)

#numbers
a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]
print(b)
c = a[::2] #optional step
print(c)

#unpacking

my_tuple = 'Max', 28, 'Boston'

name, age, city = my_tuple

print(name)
print(age)
print(city)


myt2 = [0,1,2,3,4]

i1, *i2, i3 = myt2

print(i1)
print(i3)
print(i2)
















