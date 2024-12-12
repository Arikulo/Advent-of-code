with open('puzzle.txt') as f:
    data = [x.split(';') for x in f.read().split('\n') if x]

def solve(array):
    count,power=0,0
    for place,line in enumerate(array):
        line[0] =line[0].split(':')[1]
        r,g,b=[],[],[]
        for hand in line:
            hand = hand.split(',')
            r.append(sum([int(thing.split()[0]) for thing in hand if 'red' in thing]))
            g.append(sum([int(thing.split()[0]) for thing in hand if 'green' in thing]))
            b.append(sum([int(thing.split()[0]) for thing in hand if 'blue' in thing]))

        if max(r) <= 12 and max(g) <= 13 and max(b) <= 14:
           count+=place+1
        power += max(r)*max(g)*max(b)

    print(count)
    print(power)

solve(data)