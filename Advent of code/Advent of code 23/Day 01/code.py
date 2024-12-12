
with open('puzzle.txt') as f:
    data_1 = [x for x in f.read().split('\n') if x]
    data_2 = data_1
    
def part_1(array):
    value = 0
    for line in array:
        nums = [x for x in line if x.isdigit()]
        number = int(nums[0] + nums[-1])
        value+=number
    return value
    
def part_2(array):
    replacements = {'one':'o1e','two':'t2o','three':'t3e','four':'f4r','five':'f5e',
                    'six':'s6x','seven':'s7n','eight':'e8t','nine':'n9e'}
    for place,line in enumerate(array):
        for key in list(replacements.keys()):
            line=line.replace(key,replacements[key])
        array[place]=line
    return part_1(array)
  
      
print(part_1(data_1))
print(part_2(data_2))
