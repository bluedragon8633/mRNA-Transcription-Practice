import random, sys
run = True
isRNA = True
score = 0
original = ['T','C','A','G',' ']
flipped = ['A','G','T','C',' ']
sequence = ''
answer = ''
maxScore = 0
print('Transcribe to mRNA! Type \'stop\' at any time to quit.')
if isRNA:
    flipped[2] = 'U'
while run:
    sequence = ''
    answer = ''
    for b in range(3):
        for c in range(3):
            sequence = sequence + original[random.randint(0,3)]
        if b < 2:
            sequence = sequence + ' '
    for d in range(len(sequence)):
        answer = answer + flipped[original.index(sequence[d])]
    print(sequence)
    userIn = input()
    
    if userIn == answer:
        score += 1
        maxScore += 1
        print('Correct! Score: ' + str(score) + '\n')
    elif userIn == 'stop':
        run = False
        print('Exiting program.')
    else:
        print('Incorrect. Correct answer: ' + answer)
        maxScore += 1
        if "T" in userIn:
            print('Remember, mRNA doesn\'t have T\'s!')
        print('\n')
print('Your final score is: ' + str(score) + ' out of ' + str(maxScore))
print('% correct: ' + str(float(score)/float(maxScore)*100) + '%')
if score == maxScore:
    print('Well done!')
elif score == 0:
    print('Coward.')
sys.exit()
