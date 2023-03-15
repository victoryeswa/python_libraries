name = input('Type your name: ')
print('welcome', name, 'to this adventure!')

answer = input('you are on a dirty road, it has come to an end and yu can go left or right. Which way would you like to go? ').lower()

if answer =='left':
    print('You come across a river, you walk around it or swim across')

elif answer == 'right':
    print()
else:
    print('Not a valid option. You lose!')