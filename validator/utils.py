def RepresentsInt(val):
    """
    Takes string and checks if value represents int number

    >>> RepresentsComplex('10')
    True

    >>> RepresentsComplex('Not Int!')
    False
    """
    if type(val) == int:
        return True
    try:
        if val[0] in ("-", "+"):
            return val[1:].isdigit()
        return val.isdigit()
    except:
        return False


def RepresentsFloat(val):
    """
    Takes string and checks if value represents float number

    >>> RepresentsComplex('10.1')
    True

    >>> RepresentsComplex('Am I Float?')
    False
    """
    try:
        float(val)
        return True
    except:
        return False


def RepresentsComplex(val):
    """
    Takes string and checks if value represents complex number

    >>> RepresentsComplex('10+3j')
    True

    >>> RepresentsComplex('Really Complex')
    False
    """
    try:
        complex(val)
        return True
    except:
        return False


def CanBeComparedToInt(val):
    try:
        val > 100
        return True
    except:
        return False
