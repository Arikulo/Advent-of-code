with open('puzzle.txt') as f:
    data=[x.strip() for x in f.readlines()]
    delimiter=data.index('')
    rules=[[int(a) for a in x.split('|')] for x in data[:delimiter]]
    pages=[[int(a) for a in x.split(',')] for x in data[delimiter+1:]]

incorrect=[]

def sorting(input_line,related_rules):
    starting=[x[0] for x in related_rules]
    answer=sorted(set(starting),key=starting.count,reverse=True)
    return answer + [x for x in input_line if x not in answer]

def solve():
    total=0
    incorrect=[]
    incorrect_comparisons=[]
    for line in pages:
        comparisons=[]
        for place,number in enumerate(line):
            comparisons+=[[number,line[i]] for i in range(place+1,len(line))]

        count=len([x for x in comparisons if x in rules])
        if count==len(comparisons):
            total+=line[(len(line)//2)]

        else:
            incorrect.append(line)
            incorrect_comparisons.append(comparisons)
    print(total)
    total=0

    for place,wrong in enumerate(incorrect):
        needed_rules=[]
        comparisons=incorrect_comparisons[place]
        for pair in comparisons:
            if pair in rules:
                needed_rules.append(pair)
            elif pair[::-1] in rules:
                needed_rules.append(pair[::-1])
        corrected=sorting(wrong,needed_rules)
        total+=corrected[(len(corrected)//2)]
    print(total)

solve()   
