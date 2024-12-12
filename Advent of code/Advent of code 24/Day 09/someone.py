with open('puzzle.txt') as f:
    rawinput = f.read()

lengths = [int(num) for num in rawinput]
# lengths=[1,2,3,4,5]

grid = [i//2 if i%2==0 else '.' for i,num in enumerate(lengths) for _ in range(num)]

# print(grid)
# while '.' in grid:
#     if grid[-1] == ('.'):
#         grid.pop()
#     else:
#         index = grid.index('.')
#         grid[index] = grid.pop()


empties=[x for x in range(len(grid)) if grid[x]=='.']
fill=[x for x in range(len(grid)) if grid[x]!='.'][::-1][:len(empties)]

for a,b in zip(empties,fill):
    if a>=b:
        break
    else:
        grid[a]=grid[b]
        del grid[b]
        
print(grid)

answer = sum(i*int(num) for i,num in enumerate(grid) if num!='.')
print(answer)
