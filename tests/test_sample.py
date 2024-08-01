"Blablabla mon module"

import pandas as pd

def square(x):
    """
    Square function.
    
    @param x: Numerical value
    @return: Square x
    """
    y = x**2
    return y

def test_pandas(x):
    """
    Create df.
    
    @param x: Numerical value
    @return: Square x
    """
    y = square(X)
    assert y >= 0
    df = pd.DataFrame({'x': [x], 'y': [y]})
    return df

if __name__ == '__main__':
    X = 7
    df = test_pandas(X)
    
