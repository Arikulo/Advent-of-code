with open('puzzle.txt') as f:
    data=[x.strip() for x in f.readlines()]

def part_1():
    twice,thrice=0,0
    for line in data:
        counts=[line.count(x) for x in set(line)]
        if 2 in counts: twice+=1
        if 3 in counts: thrice+=1

    print(twice*thrice)

def part_2():

    for i,string_1 in enumerate(data):

        for x in range(i,len(data)):
            one,two=[a for a in string_1],[a for a in data[x]]
            diff=[a for a,b in zip(one,two) if a!=b]
            # print(diff)
            if len(diff)==1:
                # print(x,i)
                # print(string_1,data[x],sep='\n')
                print(''.join([a for a in data[i] if a in data[x]]))
                # return

        

    

part_1()
part_2()

#0 -   aimcjvlhedbsyoqfzukjpxw
#113 - aimcjvlhedbsyoqfzukupxw