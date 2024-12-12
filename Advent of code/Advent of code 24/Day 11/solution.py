from collections import defaultdict

with open('puzzle.txt') as f:
    data=[int(a) for x in f.readlines() for a in x.strip().split()]

stuff=defaultdict(int)
for x in data:
    stuff[x] +=1


def blinking(amount):
    for _ in range(amount):
        array=dict(stuff)
        for item,amount in array.items():
                if amount == 0: continue
                if item == 0:
                     stuff[1]+=amount
                     stuff[0]-=amount
                     
                elif len(str(item)) % 2 == 0:
                     length = int(len(str(item)) / 2)
                     first = int(str(item)[:length])
                     second=int(str(item)[length:])
                     stuff[first]+=amount
                     stuff[second]+=amount
                     stuff[item]-=amount

                else:
                     stuff[item*2024]+=amount
                     stuff[item]-=amount

    print(sum(stuff.values()))


    

blinking(75)