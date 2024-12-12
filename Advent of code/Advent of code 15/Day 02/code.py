with open('puzzle.txt') as f:
    data = [line.split('x') for line in f.read().split()]


def solution():
    paper = 0
    ribbon = 0
    for l,w,h in data:
        l,w,h = int(l),int(w),int(h)
        smallest = sorted([l,w,h])
        slack = smallest[0]*smallest[1]
        perimeter = 2*(smallest[0] + smallest[1])
        s_f = 2*l*w + 2*w*h + 2*h*l
        volume = l*w*h
        paper+= s_f + slack
        ribbon += volume + perimeter
    print(paper,ribbon)
    

solution()
        
        