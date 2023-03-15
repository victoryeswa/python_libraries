print('Welcome to my computer quiz!')

playing = input('Do you want to play? ')

#.lower() converts the input into a lower case to enable it match with the output
if playing.lower() !='yes':
    quit()
print('Okay! Let\'s play :')
score = 0
answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('correct!')
    score +=1
else:
    print('incorrect!')

answer = input('What does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('correct!')
    score+=1
else:
    print('incorrect!')

answer = input('What does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('correct!')
    score+=1
else:
    print('incorrect!')
#alterntively you can convert the input directly into lower case
answer = input('What does PSU stand for? ').lower()
if answer  == 'power supply unit':
    print('correct!')
    score+=1
else:
    print('incorrect!')

#telling how many correct gueeses are there
print('You got ' +  str(score) + 'questions correct!')
print('You got ' + str((score/4)*100)+'%.')
