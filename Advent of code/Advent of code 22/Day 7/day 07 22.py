from collections import defaultdict

with open("day 07 22 test.txt") as f:
    commands = f.readlines()
   
sizes = defaultdict(int)
stack = [] 

for c in commands:
    print(stack)
    if c.startswith("$ ls") or c.startswith("dir"):
        continue
    if c.startswith("$ cd"):
        destination = c.split()[2]

        if destination == '..':
            stack.pop()
            
        else:
            path = f'_{destination}' if stack else destination
            # print(path)
            stack.append(path)
    else:
        size,file = c.split()
        for path in stack:
            sizes[path]+=int(size)
     
        
needed_size = 30000000 - (70000000 - sizes["/"])
for size in sorted(sizes.values()):
    #returns first value that meets condition
    if size > needed_size:
        break

print(sum(n for n in sizes.values() if n <= 100000)) # task 1
print(size) # task 2
     
