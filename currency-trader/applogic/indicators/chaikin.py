def ad(array):
    ''' Returns the accumulation distribution value of the array
    '''
    cross_this = 0.85
    for i in range(len(array)-1):
        # array[open, high, low, close, volume]
        ad = (array[i][3]-array[i][0]) / (array[i][1]-array[i][2]) * array[i][4]

    return ad
    
    ''' How to read:
    if ad > cross_this:
        #print('volume is there')
        return (-1)
    else:
        #print('no volume')
        return (0)
    '''