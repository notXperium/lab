import argparse

p = argparse.ArgumentParser(description="Lösen")
p.add_argument("a", type=int)
p.add_argument("b", type=int)
p.add_argument("c", type=int)
p.add_argument("d", type=int)
args = p.parse_args()


def loese(a,b,c,d):
    print(f"{a}x+{b} = {c}x+{d}\n")
    print(f"{a}x+{b} = {c}x+{d} |-{c}x")
    print(f"{a}x-{c}x+{b} = {d} |-{b}")
    print(f"{a}x-{c}x = {d}-{b} |()")
    print(f"x*({a}-{c}) = {d-b} |:({a}-{c})")
    print(f"x = ({d}-{b})/({a}-{c})")
    
    if a == c and b == d:
        print("L = R")
        x = None
        return x
    try:
        print(f"x = {(d-b)/(a-c)}")
        x = (d-b)/(a-c)
    except ZeroDivisionError:
        print("L = { }")
        x = None
    return x

loese(args.a,args.b,args.c,args.d)



