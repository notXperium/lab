import argparse

p = argparse.ArgumentParser(description="Lösen")
p.add_argument("a", type=float)
p.add_argument("b", type=float)
p.add_argument("c", type=float)
p.add_argument("d", type=float)
args = p.parse_args()


def loese(a,b,c,d):
    print(f"{a}x+{b} = {c}x+{d}\n")
    print(f"{a}x+{b} = {c}x+{d} |-{c}x")
    print(f"{a}x-{c}x+{b} = {d} |-{b}")
    print(f"{a}x-{c}x = {d}-{b} |()")
    print(f"x*({a}-{c}) = {d-b} |:({a}-{c})")
    if a == c and b != d:
        print("L = { }")
        x = None
    else:
     print(f"x = ({d}-{b})/({a}-{c})")
     if a == c and b == d:
        print("L = R")
        x = None
     else:
        print(f"x = {(d-b)/(a-c)}")
        x = (d-b)/(a-c)
    return x

loese(args.a,args.b,args.c,args.d)



