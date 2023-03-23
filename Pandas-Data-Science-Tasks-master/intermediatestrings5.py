#strings: ordered, immutable, text representation

my_string = 'Hello world'

print(my_string)
char = my_string[0:2]
print(char)

#removing a white space
my_string = '  Hello World  '
print(my_string)
my_string = my_string.strip()
print(my_string)

my_string = 'Hello world'.upper()

print(my_string)
my_string2 = 'Hello world'.lower()

print(my_string2)
#startswith
print(my_string2.startswith('Hello'))
print(my_string2.endswith('world'))

#find the index of a character
print(my_string2.find('o'))
#returns a minus one if no string is found
print(my_string2.find('pp'))

#count the number of xters
print(my_string2.count('p'))

#replace
print(my_string2.replace('world', 'universe'))
print(my_string2)

#convert a string to a list

my_string = 'how are you doing?'
my_list = my_string.split(' ')
print(my_list)

#cponvert a list to a string
new_string = ' '.join(my_list)
print(new_string)