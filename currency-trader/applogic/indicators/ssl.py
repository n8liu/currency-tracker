import numpy as np
from .sma import sma_high, sma_low, sma_close

# must take in an array of size 10 with 4 columns
def ssl(array):
    '''Returns the SSL of an array.
    '''
    hlv_array = np.zeros(len(array))

    for i in range(len(array)):
        sma_h = sma_high(array)
        sma_l = sma_low(array)
        
        if i == 0:
            hlv_array[1] = hlv_array[0]
        else:
            hlv_array[i] = hlv_array[i-1]
       
        if array[i][3] > sma_h:
            hlv_array[i] = 1
        elif array[i][3] < sma_l:
            hlv_array[i] = -1
    #print(hlv_array)
    if hlv_array[len(array) - 2] == -1 and hlv_array[len(array) - 1] == 1:
        #print('ssl', 1)
        return 1 # buy 
    elif hlv_array[len(array) - 2] == 1 and hlv_array[len(array) - 1] == -1:
        #print('ssl', -1)
        return -1 # sell
    elif hlv_array[len(array) - 2] == 1 and hlv_array[len(array) - 1] == 1:
        #print('trend up', 1)
        return 1
    elif hlv_array[len(array) - 2] == -1 and hlv_array[len(array) - 1] == -1:
        #print('trend down', -1)
        return -1
    else:
        #print(0)
        return 0