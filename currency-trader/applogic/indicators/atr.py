import numpy as np 

# take in an array of 14 rows and 4 columns.
def atr(array):
    '''Returns the average true range of an array. 
    '''
    k = 14
    tr_sum = 0
    for i in range(len(array)):
        tr_sum += max(abs(array[i][1] - array[i][2]), abs(array[i][1] - array[i][3]), abs(array[i][2] - array[i][3]))
    #print(tr_sum)
    atr = (tr_sum / k)
    #print('atr:', atr)
    return atr
