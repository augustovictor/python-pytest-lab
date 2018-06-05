def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def genericCalc(a, b, operationType):
    if operationType == 'sum':
        return add(a, b)
    elif operationType == 'sub':
        return sub(a, b)
    else:
        raise ValueError("The values must be either 'add' or 'sub'")