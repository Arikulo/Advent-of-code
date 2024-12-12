with open('puzzle.txt') as f:
    data = f.read().split()

    
    
def check(line):
    print('\n')
    nice = [0,0,0]
    vowels = {'a','e','i','o','u'}
    contains_vowels = vowels.intersection(set(line))
    if len(contains_vowels) == 5:
        print('yes 1')
        nice[0] = 1
        
    
    for thing in range(len(line)-1):
        if line[thing] == line[thing+1]:
            print('yes 2')
            nice[1] = 1
    
    not_allowed = {'ab','cd','pq','xy'}
    naughty = not_allowed.intersection(set(line))
    # print(len(naughty))
    if len(naughty) == 0:
        print('yes 3')
        nice[2] == 1
            
    print(nice)
    if sum(nice) == 3:
        return 1
    else:
        return 0
        
    print(contains_vowels)
    
def solution():
    count=0
    for line in data:
    # for i in range(10):
        
        count+=check(line)
    print(count)
    
solution()

