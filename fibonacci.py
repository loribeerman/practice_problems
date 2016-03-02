import numpy as np


def fib(n):
    '''generate array of n fibonacci numbers'''
    
    # create array of zeros to store fib numbers
    arr = np.zeros(n)
    
    if n < 2:
        return 0
    elif n == 2:
        return np.array([0, 1])
    else:
        # initialize first two fib numbers
        arr[0], arr[1] = 0, 1
        # add previous two values to get next value starting at 3rd value
        for i in range(2, len(arr)):
            arr[i] = arr[i-1] + arr[i-2]

    return arr
        


