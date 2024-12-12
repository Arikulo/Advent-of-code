with open('puzzle.txt') as f:
    data=[x.strip() for x in f.readlines()]

def part_1():
    output=[['.']*1000]*1000
    output=[x[:] for x in output]
    claims=[]

    for line in data:
        no,at,start,area=line.split(' ')

        no=no[1:]
        y,x=start[:len(start)-1].split(',')
        area_x,area_y=area.split('x')
        area_y,area_x=int(area_x),int(area_y)
        supposed=area_y*area_x
        x,y=int(x),int(y)
        claims.append((no,supposed))

        for i in range(y,y+area_y):
            for j in range(x,x+area_x):

                if output[i][j]=='.':
                    output[i][j]=no
                else:
                    output[i][j]='#'

    print(sum(row.count('#') for row in output))

    for id,expected in claims:
        # print('trying',id)
        if sum(row.count(id) for row in output) == expected:
            print(id)
            break
    
    # for line in output[300:400]:
    #     print(line[10:30]




part_1()