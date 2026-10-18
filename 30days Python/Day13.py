language = 'Python'

lst = [i for i in language]
print(lst)    

even_numbers = [i for i in range(0,21,2) if i > 0]
print(even_numbers)

x = lambda p1,p2: p1+p2
print(x(1,2))

def power(x):
    return lambda n: x ** n

print(power(2)(5))

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [i for i in numbers if i <= 0]
print(numbers)

list = []
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in list_of_lists:
    for u in i:
        list.append(u)
print(list)