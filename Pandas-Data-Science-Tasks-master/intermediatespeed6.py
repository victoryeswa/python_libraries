from timeit import default_timer as timer

my_list = ['a'] * 6
print(my_list)

#bad
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop-start, 'bad code')

#good code
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop-start, 'good code')
# using the f-string
var = 3.1234
var2 = 6
my_string = f'the variable is {var} and {var2}'
print(my_string)