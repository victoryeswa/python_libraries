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