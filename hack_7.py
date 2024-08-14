"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    i = 0
    while i <= 5:
        result.insert(0, i)
        i += 1
    return result