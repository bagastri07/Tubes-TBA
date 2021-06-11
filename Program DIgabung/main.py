from lexical_analyzer import lexical_analyzer
from parser_grammar import parser

print('=====Proses Lexycal Analyzer=====')
sentence = input('Masukan Kalimat: ')
if (lexical_analyzer(sentence)):
    print('\n=====Proses Parsing=====')
    parser(sentence)
else:
    print('\nSentence tidak valid, tidak dapat diproses di parser')
