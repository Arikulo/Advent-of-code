from itertools import groupby
import re
import numpy as np

with open('day 11 22 data.txt') as f:
    in_data = [x[:-1] for x in f.readlines()]
    
def calc(operation):
    if len(operation) == 2:
        a,b,c=1,0,0
    elif operation[0] == '*':
        a,b,c=0,int(operation[1]),0
    elif operation[0] == '+':
        a,b,c = 0,0,int(operation[1])
        
    return a,b,c

def monkey_stuff():
    monkey_data = []
    data = [list(group) for ele, group in groupby(in_data,key=bool) if ele]
    for monkeys in data:
        items = [int(x) for x in re.findall(r'\d+',monkeys[1])]
        
        operation = sorted(set((monkeys[2][19:].split())))
        a,b,c = calc(operation)
        divisor = int(re.findall(r'\d+',monkeys[3])[0])
        if_true = int(re.findall(r'\d+',monkeys[4])[0])
        if_false = int(re.findall(r'\d+',monkeys[5])[0])
        
        monkey_data.append([items,[a,b,c],divisor,[if_true,if_false]])
    return monkey_data
    
def solution(choice,amount):
    monkey_data =monkey_stuff()
    inspections = [0]*len(monkey_data)
    lcm = np.prod([monkey_data[n][2] for n in range(len(monkey_data))])
    for _ in range(amount):
        for place,(items,(a,b,c),divisor,(yes,no)) in enumerate(monkey_data):
            if choice == 1:
                
                if c != 0:
                    worries = [int(np.floor((x+c)/3)) for x in items]
                else:
                    worries = [int(np.floor((a*x**2 + b*x)/3)) for x in items]
            if choice == 2:
                if c != 0:
                    worries = [int(np.floor((x+c)%lcm)) for x in items]
                else:
                    worries = [int(np.floor(a*x**2 + b*x)%lcm) for x in items]
                
            inspections[place]+=len(worries)
            removes = []
            for value_place,value in enumerate(worries):
                
                if value % divisor == 0:
                    removes.append(value_place)
                    monkey_data[yes][0].append(value)
                elif value % divisor != 0:

                    removes.append(value_place)
                    monkey_data[no][0].append(value)

            for x in sorted(removes,reverse=True):
                monkey_data[place][0].pop(x)
                    
    i_s = sorted(inspections,reverse=True)
    print(i_s[0]*i_s[1])
  
    
solution(1,20)
solution(2,10000)
