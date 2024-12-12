from functools import cmp_to_key
from math import prod

def compare(l,r):
    
    match l, r:
        case int(),int():
            # if l>r, returns True - False = 1
            # if l<r, returns False - True = -1
            # if l=r, returns False - False = 0
            return (l>r) - (l<r)
        case int(),list():
            #turns l into a list if its an int
            return compare([l],r)
        case list(),int():
            #turns r into a list if its an int
            return compare(l,[r])
        case list(),list():
            #compares each value in l,r if they're both lists
            for z in map(compare,l,r):
                if z:
                    return z
            return compare(len(l), len(r))
 

packets = [[*map(eval, x.split())] for x in open('day 13 22 data.txt').read().split('\n\n')]
print(sum(i for i, p in enumerate(packets, 1) if compare(*p) == -1))

# packets = sorted(sum(packets, [[2], [6]]), key=cmp_to_key(compare))
# print(prod(i for i, p in enumerate(packets, 1) if p in [[2], [6]]))


    
