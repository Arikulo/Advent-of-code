from collections import defaultdict

with open("day 07 22 data.txt") as f:
    commands = f.readlines()

sizes = defaultdict(int)
stack = []


for c in commands:

    if c.startswith("$ ls") or c.startswith("dir"):
        # list or dir name, either way line doesn't matter
        continue
    if c.startswith("$ cd"):
        #start of dir
        dest = c.split()[2] # destination
        if dest == "..":
            #end of dir
            stack.pop() # remove current dir from stack
        else:
            # print(stack,dest)
            path = f"{stack[-1]}_{dest}" if stack else dest # accounts for first overall dir
            # 'stack' is the directory to get to any item, 
            stack.append(path)
    else:
        #file
        size, file = c.split()
        for path in stack:
            #adds dir to dict with value of size
            sizes[path] += int(size)
   

needed_size = 30000000 - (70000000 - sizes["/"])
for size in sorted(sizes.values()):
    #returns first value that meets condition
    if size > needed_size:
        break

print(sum(n for n in sizes.values() if n <= 100000)) # task 1
print(size) # task 2
