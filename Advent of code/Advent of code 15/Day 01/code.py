data = open('puzzle.txt').read()

print(data.count(sorted(set(data))[0]) -data.count(sorted(set(data))[1]))

elevator = {'(':1,')':-1}
start = 0

for place,thing in enumerate(data):
    start +=elevator[thing]
    if start == -1:
        print(place+1)
        break