import numpy as np
with open('puzzle.txt') as f:
    data = [x.strip() for x in f.readlines()]
 
def part_1():
    freqs=[]
    total=0
    for line in data:
        operator=line[0]
        num=int(line[1:])
        if operator=='+':
            total+=num
        else:
            total-=num
        freqs.append(total)
    print(total)
    freqs=np.array(freqs)
    for i in range(1,10000):
        test=freqs+i*total
        answer=[x for x in test if x in freqs]
        if answer:
            print(answer[0])
            return
            
    
part_1()
