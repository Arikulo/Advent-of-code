with open('puzzle.txt') as f:
    data = [list(map(int, line.replace(':','').split())) for line in f]

def add(a,b): return a+b

def mul(a,b): return a*b

def cot(a,b): return int(str(a)+str(b))

def solve(nums,ops):
    if len(nums) == 2:
        return nums[0] == nums[1]
    total, a, b, *rest = nums
    for op in ops:
        if solve([total, op(a, b)] + rest, ops):
            return total
    return 0


def part_1():

    print(sum([solve(line, ops=[add, mul]) for line in data]))
    print(sum([solve(line, ops=[add,mul,cot]) for line in data]))

part_1()
