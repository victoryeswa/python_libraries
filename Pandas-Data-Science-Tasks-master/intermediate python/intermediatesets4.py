# sets: unordered, mutable, no duplicates

myset = set('helloo')
myset2 = {1, 2, 3, 4, 5, 6}

print(myset)
print(myset2)

#mutable
myset = set()

myset.add(1)
myset.add(2)
myset.remove(1)
#
myset.discard(4)

#pop method - return an arbitrary value
print(myset2.pop())

#iterate

for i in myset2:
    print(i)
#to check for an element

if 2 in myset2:
    print('yes')
else:
    print('No')


odds = {1,3,5,7,9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5,7}

#union

u = odds.union(evens)
print(u)

#INTERSECTION

i = odds.intersection(primes)

print(i)


setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)

print(diff, 'setA/setB')

diff2 = setB.difference(setA)

print(diff2, 'setB/setA')

#symmetric difference method
diff3 = setB.symmetric_difference(setA)
diff4 = setA.symmetric_difference(setB)

print(diff3, 'setB/setA, symmetric difference')
print(diff4, 'setA/setB symmetric difference')
#update method
setA.update(setB)

print(setA)

#intersection update method

setA.intersection_update(setB)

print(setA)

#difference update method

setA.difference_update(setB)  # updates by removing elements found in another set
print(setA)
#symmetric difference update
#updates the element that is found in set A or B but not in both

setA.symmetric_difference_update(setB)
print(setA)

setA = {1,2,3,4,5,6}
setB = {1, 2,3}

print(setA.issubset(setB)) #false
print(setA.issuperset(setB)) #true

print(setA.isdisjoint(setB)) #false

#frozen set - immutable version of a normal set
a = frozenset([1,2,3,4])

print(a) #immutable




















