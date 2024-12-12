with open('puzzle.txt') as f:
    data=[x.strip() for x in f.readlines()]


def diff(array,a,b):
    return (array[b][0]-array[a][0],array[b][1]-array[a][1]) 

def solve(amount,yes):
    lines,line_length=len(data),len(data[0])
    grid=[['.']*line_length]*lines
    grid=[x[:] for x in grid]
    antennas=set([a for x in data for a in x if a!='.'])
    total=0
    for freq in antennas:
        positions=[(j,i) for i in range(lines) for j in range(line_length) if data[i][j]==freq]
        antinodes=[]

        for i in range(len(positions)):
            distances=[diff(positions,i,x) for x in range(i+1,len(positions))]
            node_x,node_y=positions[i]
            if yes:
                antinodes.append((node_x,node_y))
            if distances:
                for dx,dy in distances:
                    for i in range(1,amount+1):
                        antinodes.append((node_x+(i+1)*dx,node_y+(i+1)*dy))
                        antinodes.append((node_x-i*dx,node_y-i*dy))

        for position in antinodes:
            if position[0]>=0 and position[0]<line_length and position[1]>=0 and position[1]<lines:
                grid[position[1]][position[0]]='#'        


    for line in grid:
        line=''.join(line)
        # print(line)
        total+=line.count('#')

    print(total)


solve(1,False)
solve(2000,True)
    
