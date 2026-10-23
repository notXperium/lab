lst = []
lst2 = ["a","b","c","d","e"]
for i in lst2:
    lst.append(i)

print(lst)
print(len(lst))
print(lst[round(len(lst) / 2)])
print(lst[len(lst) -1])

mixed = ["name", 18, 187, "married"]
it = list()
it += ["A", "B"]

for i in mixed:
    print(i)

mixed.extend(it)

for i in mixed:
    print(i)

print("A" in mixed)

del lst
print(lst2.sort(reverse=True))

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("min: ", ages[0], "\nmax: ", ages[len(ages) -1])
print("median: ", sum(ages)/len(ages))
