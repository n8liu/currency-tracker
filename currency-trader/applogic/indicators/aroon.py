import numpy as np 

# must take in an array of size 6
def aroon(array):
    '''Returns the buy/sell signal of Aroon Indicator
    '''
    k = 6
    maxi = 0
    mini = 0
    max_dev = 0
    min_dev = 0
    for i in range(len(array)):
        if i == 0:
            maxi = array[0][1] #high
            mini = array[0][2] #low
        if array[i][1] > maxi:
            maxi = array[i][1]
        elif array[i][2] < mini:
            mini = array[i][2]
        elif array[i][1] < maxi:
            max_dev += 1
        elif array[i][2] > mini:
            min_dev += 1
    a_up = ((k - max_dev) / k) * 100
    a_down = ((k - min_dev) / k) * 100

    return [a_up, a_down]

    ''' How to read the indicator:
    if a_up > a_down:
        #print('aroon', 1)
        return 1 # buy 
    elif a_up < a_down:
        #print('aroon', -1)
        return -1 # sell
    else:
        #print('aroon', 0)
        return 0
    '''

