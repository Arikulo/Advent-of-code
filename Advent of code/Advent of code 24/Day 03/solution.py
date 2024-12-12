import re
with open('puzzle.txt') as f:
    data=[x.strip() for x in f.readlines()]
    
def part_1():
    answer=0
    muls=[x for line in data for x in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)',line)]
    for prod in muls:
        prod=prod.split(',')
        a=int(prod[0].split('(')[1])
        b=int(prod[1].split(')')[0])
        answer+=a*b
    print(answer)

def part_2():
    answer=0
    muls=[x for line in data for x in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)',line)]
    yes=True
    for prod in muls:
        if prod == 'do()':
            yes=True
        elif prod == "don't()":
            yes=False
        elif yes:
            prod=prod.split(',')
            a=int(prod[0].split('(')[1])
            b=int(prod[1].split(')')[0])
            answer+=a*b
    print(answer)
    
        
part_1()
part_2()
