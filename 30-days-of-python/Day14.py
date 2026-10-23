def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']

n = [1,2,3,4,5,6]
y =lambda x: x**2
s = map(y, n)
print(list(s))

e = lambda z: True if z % 2 == 0 else False
print(list(filter(e, n)))

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

cb = lambda c: c.upper()

print(list(map(cb, countries)))

cm = lambda z: True  if len(z) == 6 else False

print(list(filter(cm, countries)))

