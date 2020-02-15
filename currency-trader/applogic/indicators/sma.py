import numpy as np

# using candlestick highest
def sma_high(array):
    sigma = 0
    
    for i in range(len(array)):
        sigma += array[i][1]

    sma = sigma / len(array)

    return sma

# using candlestick low
def sma_low(array):
    sigma = 0

    for i in range(len(array)):
        sigma += array[i][2]

    sma = sigma / len(array)

    return sma

# using candlestick close (default)
def sma_close(array):
    sigma = 0

    for i in range(len(array)):
        sigma += array[i][3]
        
    sma = sigma / len(array)
    
    return sma


    


