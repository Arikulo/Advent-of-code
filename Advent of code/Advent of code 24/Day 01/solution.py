
with open('puzzle.txt') as f:
    data=[a.split() for x in f.readlines() for a in x.split('\n') if a]
    first=sorted([int(x[0]) for x in data])
    second=sorted([int(x[1]) for x in data])

def part_1(arr_1,arr_2):
    count=0
    for i in range(len(arr_1)):
        count+=abs(arr_1[i]-arr_2[i])
    print(count)

def part_2(arr_1,arr_2):
    count=0
    for i in arr_1:
        count+=i*arr_2.count(i)
    print(count)

part_1(first,second)
part_2(first,second)