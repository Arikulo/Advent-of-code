data = open('puzzle.txt').read()
# data='>'
# data='^v'
# data = '^>v<'
# data='^v^v^v^v^v'
movements = {'^':(0,1),'v':(0,-1),'>':(1,0),'<':(-1,0)}

def houses(data_set):
    start = [0,0]
    output_list = [str(start)]
    for command in data_set:
        start = [a+b for a,b in zip(start,movements[command])]
        output_list.append(str(start))
    return output_list
        
    

def solution():
    part_1 = houses(data)

    santa = houses(data[::2])
    robo = houses(data[1::2])
    print(len(set(part_1))) 
    
    santas = santa + robo
    print(len(set(santas)))
    print('\n')
    

solution()


#day 4
import hashlib

def day_4(n):
    for i in range(10000000):
        string = 'bgvyzdsv' + str(i)
        result = hashlib.md5(string.encode()).hexdigest()
    
        if result[:n] == '0'*n:
            print(i)
            break

day_4(5)
day_4(6)