def addition(a, b):
    result = a + b
    return result

def multiplication(a, b):
    result = a * b
    return result

def division(a, b):
    result = a / b
    return result


print('((5+2)*10)/2 =', division(multiplication(addition(5, 2), 10), 2))