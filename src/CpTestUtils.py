from random import randint

# returns a one-dimensional array of optionally
# random integers between minimum and maximum
def intArray1D(l, isRand, minimum, maximum):
    return [min(i + minimum, maximum) if not isRand \
            else randint(minimum, maximum) \
            for i in range(l)]

# returns a two-dimensional array of optionally
# random integers between minimum and maximum
def intArray2D(m, n, isRand, minimum, maximum):
    return [[min((i * n + j) + minimum, maximum) if not isRand \
             else randint(minimum, maximum) \
            for j in range(n)] \
           for i in range(m)]

# returns a random binary matrix, can be string elements or ints
def binaryMatrix(m, n, isString):
    return [[str(randint(0, 1)) if isString else randint(0, 1) \
             for _ in range(m)] \
            for _ in range(n)]

# returns a string with random characters between
# chars minimum and maximum (i.e. if minimum is 'a'
# and maximum is 'd', will have chars 'a' 'b' 'c' 'd')
def string(l, minimum, maximum):
    return '"' + ''.join([chr(randint(ord(minimum), ord(maximum))) \
                          for _ in range(l)]) + '"'

