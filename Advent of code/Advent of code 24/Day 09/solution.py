with open('test.txt') as f:
    data=[int(x) for x in f.readlines()[0]]

def part_1():
    output=[]
    for place,thing in enumerate(data):
        if (place+1)%2 == 0:
            output+='.'*thing
        else:
            output+=[f'{place//2}']*thing

    output=[int(x) if x!='.' else '.' for x in output]
    empties=[x for x in range(len(output)) if output[x]=='.']
    fill=[x for x in range(len(output)) if output[x]!='.'][::-1][:len(empties)]
    for a,b in zip(empties,fill):
        if a>=b:
            break
        else:
            output[a]=output[b]
            output[b]='.'
        
    total=sum([i*int(output[i]) for i in range(len(output)) if output[i]!='.'])
    print(total)
        
def part_2():
    output=[]
    empties=[]
    fill=[]
    for place,thing in enumerate(data):
        if (place+1)%2 == 0:
            empties.append((len(output),thing))
            output+='.'*thing

        else:
            fill.append((len(output),thing))
            output+=[f'{place//2}']*thing
            

    output=[int(x) if x!='.' else '.' for x in output]
    # fill=fill[::-1]

    print(output,empties,fill,sep='\n')

# part_1()
part_2()

