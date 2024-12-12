with open('puzzle.txt') as f:
    data=[list(x.strip()) for x in f.readlines()]

def up(x,y): return x, y-1

def down(x,y): return x, y+1

def left(x,y): return x-1, y

def right(x,y): return x+1, y

directions=[up,right,down,left]
start_x,start_y=[(x,y) for y,line in enumerate(data) for x, char in enumerate(line) if char=='^'][0]
visited=[]

def part_1():
    x,y=[(x,y) for y,line in enumerate(data) for x, char in enumerate(line) if char=='^'][0]
    place=0
    while (x>=0 and x<len(data[0])) and (y>=0 and y<len(data)):
        x_next,y_next=directions[place](x,y)
        if x_next>=len(data[0]) or y_next>=len(data):
            break
        if data[y_next][x_next] == '#':
            place=(place+1)%4

        else:
            x,y=directions[place](x,y)
            if (x,y) not in visited:
                visited.append((x,y))

    print(len(visited))


def loop(start,place):
    answer=0
    x,y=start
    # x,y=x,y=[(x,y) for y,line in enumerate(data) for x, char in enumerate(line) if char=='^'][0]

    visit={(x,y):1}
    # place=0
    while (x>=0 and x<len(data[0])) and (y>=0 and y<len(data)):    # will end when outside range
        x_next,y_next=directions[place](x,y)

        if x_next>=len(data[0]) or y_next>=len(data):    # gone outsite range
            break
        
        if max(visit.values())>=10:    # if visited any spot 3 times, it must be a loop
            answer=1
            break

        if data[y_next][x_next] == '#':    # rotates direction 90 degrees
            place=(place+1)%4

        else:   # moves foreward and adds to history
            x,y=directions[place](x,y)
            # data[y][x]='#'
            if (x,y) in visit:
                visit[(x,y)]+=1
            else:
                visit[(x,y)]=1

    return answer,place


def part_2():
    total=0
    check=visited
    length=len(check)
    last_block=[(x,y) for y,line in enumerate(data) for x, char in enumerate(line) if char=='^'][0]
    direction=0
    for place in range(len(check)):
        print(place+1,length)

        block=check[place]
        block_x,block_y=block

        data[block_y][block_x]='#'
        direction=0
        result,direction=loop(last_block,direction)
        total+=result
        data[block_y][block_x]='.'
        # last_block=block
    print(total)

part_1()
# visited.remove((start_x,start_y))
part_2()