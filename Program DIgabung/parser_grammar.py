def parser(sentence):
    tokens = sentence.lower().split()
    tokens.append('EOS')

    nonTerminals = ['S', 'N', 'V']
    terminals = ['abah', 'uma', 'banyu', 'kupiah', 'andak',
                'maulah', 'kulahai', 'wadah', 'baisi', 'lajak']

    parseTable = {}

    parseTable[('S', 'abah')] = ['N', 'V', 'N']
    parseTable[('S', 'uma')] = ['N', 'V', 'N']
    parseTable[('S', 'banyu')] = ['N', 'V', 'N']
    parseTable[('S', 'kupiah')] = ['N', 'V', 'N']
    parseTable[('S', 'wadah')] = ['N', 'V', 'N']
    parseTable[('S', 'andak')] = ['error']
    parseTable[('S', 'maulah')] = ['error']
    parseTable[('S', 'kulahai')] = ['error']
    parseTable[('S', 'baisi')] = ['error']
    parseTable[('S', 'lajak')] = ['error']
    parseTable[('S', 'EOS')] = ['error']

    parseTable[('N', 'abah')] = ['abah']
    parseTable[('N', 'uma')] = ['uma']
    parseTable[('N', 'banyu')] = ['banyu']
    parseTable[('N', 'kupiah')] = ['kupiah']
    parseTable[('N', 'wadah')] = ['wadah']
    parseTable[('N', 'andak')] = ['error']
    parseTable[('N', 'maulah')] = ['error']
    parseTable[('N', 'kulahai')] = ['error']
    parseTable[('N', 'baisi')] = ['error']
    parseTable[('N', 'lajak')] = ['error']
    parseTable[('N', 'EOS')] = ['error']

    parseTable[('V', 'abah')] = ['error']
    parseTable[('V', 'uma')] = ['error']
    parseTable[('V', 'banyu')] = ['error']
    parseTable[('V', 'kupiah')] = ['error']
    parseTable[('V', 'wadah')] = ['error']
    parseTable[('V', 'andak')] = ['andak']
    parseTable[('V', 'maulah')] = ['maulah']
    parseTable[('V', 'kulahai')] = ['kulahai']
    parseTable[('V', 'baisi')] = ['baisi']
    parseTable[('V', 'lajak')] = ['lajak']
    parseTable[('V', 'EOS')] = ['error']

    stack = []
    stack.append('#')
    stack.append('S')

    idxToken = 0
    symbol = tokens[idxToken]

    while (len(stack) > 0):
        top = stack[len(stack)-1]
        print('top = ', top)
        print('symbol = ', symbol)
        if top in terminals:
            print('top adalah simbol terminal')
            if top == symbol:
                stack.pop()
                idxToken += 1
                symbol = tokens[idxToken]
                if symbol == 'EOS':
                    print('isi stack: ', stack)
                    stack.pop()
            else:
                print('error')
                break
        elif top in nonTerminals:
            print('top adalah simbol non-terminal')
            if parseTable[(top, symbol)][0] != 'error':
                stack.pop()
                symboltobePushed = parseTable[(top, symbol)]
                for i in range(len(symboltobePushed)-1, -1, -1):
                    stack.append(symboltobePushed[i])
            else:
                print('error')
                break
        else:
            print('error')
            break
        print('isi stack: ', stack)
        print()

    print()
    if symbol == 'EOS' and len(stack) == 0:
        print('Input string ', sentence, ' diterima, sesuai grammar')
    else:
        print('Error, Input string: ', sentence, 'ditolak, tidak sesuai grammar')