
with open("Advent of code 23/Day 03/test.txt") as f:
    punctuation = ['*','&','+','/','#','$']
    data = [x for x in f.read().split('\n') if x]
    puncts=[(count,line.index(x)) for count,line in enumerate(data) for x in punctuation if x in line]
    stars=[(count,line.index('*')) for count,line in enumerate(data) if '*' in line]


def check(x,y):
    area=[data[x-1][y-1:y+2],data[x][y-1],data[x][y+1],data[x+1][y-1:y+2]]
    area=[thing.replace('.','') for thing in area]
    return area


for x,y in puncts:
    # x,y=pair
    print(x,y)
    places=check(x,y)

    print(places)
