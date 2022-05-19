import random

isRNA = True
score = 0
original = ['T','C','A','G',' ']
flipped = ['A','G','T','C',' ']
sequence = ''
answer = ''

print('Transcribe to mRNA!')
if isRNA:
    flipped[2] = 'U'
for a in range(5):
    sequence = ''
    answer = ''
    for b in range(4):
        for c in range(3):
            sequence = sequence + original[random.randint(0,3)]
        if b < 3:
            sequence = sequence + ' '
    for d in range(len(sequence)):
        answer = answer + flipped[original.index(sequence[d])]
    print(sequence)
    userIn = input()
    if userIn == answer:
        score += 1
        print('Correct! Score: ' + str(score) + '\n')
    else:
        print('Incorrect. Correct answer: ' + answer)
        if "T" in userIn:
            print('Remember, mRNA doesn\'t have T\'s!')
        print('\n')
print('Your final score is: ' + str(score))
