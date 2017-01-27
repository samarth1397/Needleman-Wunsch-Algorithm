import numpy as np
import matplotlib.pyplot as plt


match_score=int(input('Enter Match Score: '))
mismatch_score=int(input('Enter Mismatch score: '))
gap_penalty=int(input('Enter gap penalty: '))

sequence_1=input('Enter sequence 1: ')

sequence_2=input('Enter sequence 2: ')

len_1=len(sequence_1)
len_2=len(sequence_2)

array=np.zeros(shape=(len_1+1,len_2+1))

def p(i,j):
    if sequence_1[i]==sequence_2[j]:
        return match_score
    else:
        return mismatch_score

for i in range(0,len(sequence_1)+1):
    for j in range(0,len(sequence_2)+1):
        if i==0:
            array[0,j]=gap_penalty*j
        elif j==0:
            array[i,0]=gap_penalty*i
        else:
            array[i,j]=max(array[i-1,j-1]+p(i-1,j-1),array[i-1,j]+gap_penalty,array[i,j-1]+gap_penalty)
        

print(array)




