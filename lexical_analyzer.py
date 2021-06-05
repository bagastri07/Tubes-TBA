import string

sentence = 'abah uma wadah'
inputString = sentence.lower()+'#'

alphabetList = list(string.ascii_lowercase)
stateList = ['q0', 'q1', 'q2',  'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
            'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
            'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
            'q31']

transitionTable = {}

for state in stateList:
    for alphabet in alphabetList:
        transitionTable[(state, alphabet)] = 'error'
    transitionTable[(state, '#')] = 'error'
    transitionTable[(state, ' ')] = 'error'

transitionTable['q0', ' '] = 'q0'

#abah
transitionTable[('q0', 'a')] = 'q1'
transitionTable[('q1', 'b')] = 'q2'
transitionTable[('q2', 'a')] = 'q3'
transitionTable[('q3', 'h')] = 'q6'

#uma
transitionTable[('q0', 'u')] = 'q4'
transitionTable[('q4', 'm')] = 'q5'
transitionTable[('q5', 'a')] = 'q6'

#wadah
transitionTable[('q0', 'w')] = 'q8'
transitionTable[('q8', 'a')] = 'q9'
transitionTable[('q9', 'd')] = 'q2'
transitionTable[('q2', 'a')] = 'q3'
transitionTable[('q3', 'h')] = 'q6'

#acceptable
transitionTable[('q6', ' ')] = 'q7'
transitionTable[('q6', '#')] = 'accept'
transitionTable[('q7', ' ')] = 'q7'
transitionTable[('q7', '#')] = 'accept'

#final state back 
transitionTable[('q7', 'a')] = 'q1'
transitionTable[('q7', 'u')] = 'q4'
transitionTable[('q7', 'w')] = 'q8'





idxChar = 0
state = 'q0'
currenToken = ''
while state != 'accept':
    currenChar = inputString[idxChar]
    currenToken += currenChar
    state = transitionTable[(state, currenChar)]
    if state == 'q6':
        print('Current token:', currenToken, ', valid')
        currenToken = ' '
    if state == 'error':
        print('Current token:', currenToken, ', Error')
        break
    idxChar += 1

if state == 'accept':
    print('Semua token di input: ', sentence, ', valid')