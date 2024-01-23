'''
CIS 122 Spring 2022 Project 7-1
Author: [Steven Sanchez-Jimenez]
Credits: [CIS 122 Resources]
Project: In the Loop (DNA to RNA Transcription)
'''

import doctest


def transcribe1(S):
    '''This function will convert DNA input into RNA

    >>> transcribe1('ACGT TGCA')  # data may need to be cleaned up a bit
    'UGCAACGU'
    >>> transcribe1('GATTACA')
    'CUAAUGU'
    >>> transcribe1('GAtTtTACA')  # data may need to be cleaned up a bit
    'CUAAUGU'
    >>> transcribe1('TTt ACT')    # data may need to be cleaned up a bit
    'AAUGA'
    >>> transcribe1('cs5')        # lowercase doesn't count
    '''
    str = ""
    for i in S:
        if i == 'A':
            str += 'U'
        elif i == 'C':
            str += 'G'
        elif i == 'G':
            str += 'C'
        elif i == 'T':
            str += 'A'
    if len(str) > 0:
        return str
    else:
        return 
    

def transcribe2(S):
    '''This function will convert DNA input into RNA

    >>> transcribe1('ACGT TGCA')  # data may need to be cleaned up a bit
    'UGCAACGU'
    >>> transcribe1('GATTACA')
    'CUAAUGU'
    >>> transcribe1('GAtTtTACA')  # data may need to be cleaned up a bit
    'CUAAUGU'
    >>> transcribe1('TTt ACT')    # data may need to be cleaned up a bit
    'AAUGA'
    >>> transcribe1('cs5')        # lowercase doesn't count
    '''
    str = ""
    counter = 0
    while counter < len(S):
        if S[counter] == 'A':
            str += 'U'
        elif S[counter] == 'C':
            str += 'G'
        elif S[counter] == 'G':
            str += 'C'
        elif S[counter] == 'T':
            str += 'A'
        counter +=1
    return str
        
    

print (transcribe1('ACGTTGCA'))
print (transcribe1('GATTACA'))
print (transcribe1('GATTTTACA')) 
print (transcribe1('TTTACT')) 
print (transcribe1('cs5'))

print (transcribe2('ACGTTGCA'))
print (transcribe2('GATTACA'))
print (transcribe2('GATTTTACA')) 
print (transcribe2('TTTACT')) 
print (transcribe2('cs5'))


print(doctest.testmod())






    
