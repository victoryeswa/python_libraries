#provide alternatives unlike dictionaries, tuples etc

#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

a = 'aaaabbbbccc'

my_counter = Counter(a)

print(my_counter)

print(my_counter.items(), 'items')

print(my_counter.keys(), 'keys')

print(my_counter.values(), 'values')

#most common element
print(my_counter.most_common(1)[0][0])

print(list(my_counter.elements()))


from collections import namedtuple

Point = namedtuple('Point', 'x,y')

pt = Point(1,-4)

print(pt)

print(pt.x, pt.y)

from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict['a']  = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

from collections import defaultdict
#default values of the key has not been set
#create a default key

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
print(d['a'])
print(d['c'])

from collections import deque
#can be used to add or remove elements from both ends

d = deque()

d.append(1)
d.append(2)

print(d, 'd')
#add elements
d.appendleft(3)
print(d, 'd')

#remover emelents, can be done from both sides
#pop method will return and remove the last element
d.pop()

print(d)

d.popleft()
#will return and remove the element on the left
print(d)

d.clear # wil remove all eelements

# extend, will add elements to the right
d.extend([4,5,6])

print(d)

d.extendleft([9, 7, 6])

print(d)

#rotate deque
d.rotate(1)  #all elements oon eplace to the right

print(d)