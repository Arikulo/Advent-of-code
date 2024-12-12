with open('puzzle.txt')as f:
    data=[x.strip() for x in f.readlines()]

# print(data)

def checker_1(point):
    x_max,y_max=len(data[0]),len(data)
    x,y=point
    check=['left','right','up','down','left-up','left-down','right-up','right-down']
    empty=[]

    if x-3<0: #left
        empty.append('left')
        empty.append('left-up')
        empty.append('left-down')

    if x+4>x_max: #right
        empty.append('right')
        empty.append('right-up')
        empty.append('right-down')

    if y-3<0: #up
        empty.append('up')
        empty.append('left-up')
        empty.append('right-up')


    if y+4>y_max: #down
        empty.append('down')
        empty.append('left-down')
        empty.append('right-down')

    return [x for x in check if x not in empty]

def checker_2(point):
    x_max,y_max=len(data[0]),len(data)
    x,y=point
    if x == x_max -1 or y == y_max -1 or x == 0 or y == 0:
        return False
    return True

def wordsearch_2(point,total):
    count=0
    x,y=point
    check = checker_2(point)
    words=['MAS','SAM']
    if check:
        blackslash = data[y-1][x-1] + data[y][x] + data[y+1][x+1]
        foreslash = data[y+1][x-1] + data[y][x] + data[y-1][x+1]
        if blackslash in words and foreslash in words:
            count+=1
    return count


def wordsearch_1(point,total):
    count=0
    x,y=point
    check=checker_1(point)
    word='XMAS'
    for direction in check:
        if direction == 'left':
            text=data[y][x-3:x+1][::-1]
            if text==word:
                count+=1

        elif direction == 'right':
            text=data[y][x:x+4]
            if text==word:
                count+=1
 
        elif direction == 'up':
            text=data[y][x] + data[y-1][x] + data[y-2][x] + data[y-3][x]
            if text==word:
                count+=1             
    
        elif direction == 'down':
            text=data[y][x] + data[y+1][x] + data[y+2][x] + data[y+3][x]
            if text==word:
                count+=1
            
        elif direction == 'left-up':
            text = data[y][x] + data[y-1][x-1] + data[y-2][x-2] + data[y-3][x-3]
            if text==word:
                count+=1
            
        elif direction == 'left-down':
            text = data[y][x] + data[y+1][x-1] + data[y+2][x-2] + data[y+3][x-3]
            if text==word:
                count+=1
      
        elif direction == 'right-up':
            text = data[y][x] + data[y-1][x+1] + data[y-2][x+2] + data[y-3][x+3]
            if text==word:
                count+=1  
            
        elif direction == 'right-down':
            text = data[y][x] + data[y+1][x+1] + data[y+2][x+2] + data[y+3][x+3]
            if text==word:
                count+=1
                
    return count
            
        
def part_1():
    crosses=[(i,place) for place,line in enumerate(data) for i in range(len(line)) if line[i]=='X']
    count=0
    for point in crosses:
        count+=wordsearch_1(point,count)
    print(count)

def part_2():
    centres=[(i,place) for place,line in enumerate(data) for i in range(len(line)) if line[i]=='A']
    count=0
    for point in centres:
        count+=wordsearch_2(point,count)
    print(count)

part_1()
part_2()