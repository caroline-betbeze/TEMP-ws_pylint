"Blablabla mon module"

import pandas as pd

def square(x):
    """
    Square function.
    
    @param x: Numerical value
    @return: Square x
    """
    y = x**2
    assert y >= 0
    return y

if __name__ == '__main__':
    X = 7
    square(X)
