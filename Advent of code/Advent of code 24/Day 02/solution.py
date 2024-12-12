
with open('puzzle.txt') as f:
    data=[a.split() for x in f.readlines() for a in x.split('\n') if a]


def run_again(line):

    for i in range(len(line)):
        test=[line[x] for x in range(len(line)) if x!=i]
        if check_diff(test):
            return True
    return False

def check_diff(line):
    diffs=[int(line[i])-int(line[i-1]) for i in range(1,len(line))]
    return (max(diffs)<=3 and min(diffs)>=1) or (max(diffs)<=-1 and min(diffs)>=-3)


def part_1(stuff):
    count=0
    yes=0
    for report in stuff:
        if check_diff(report):
            count+=1
        elif run_again(report):
            yes+=1
    print(count,count+yes)

part_1(data)