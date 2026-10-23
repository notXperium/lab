try:
    x=44
    print(x)
except NameError:
    print("x")
except:
    print("x gibts nix")
else:
    print(x)
finally:
    print("lol")


y = lambda z,t: z+t
list = [1,2]
print(y(*list))


country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

print(nordic_countries.index("Finland"))
aa = []
for a,b in zip(country_lst_one, country_lst_two):
    aa.append({a, b})

print(aa)