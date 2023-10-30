def part1(filename):
    packets = parse(open(filename).read())
    correct = []
    for i in range(0, len(packets), 2):
        if compare(packets[i], packets[i + 1]) < 0:
            correct.append((i // 2) + 1)
    return sum(correct)
    
# v1 is smallest -> return negative
# v2 is smallest -> return positive
# equal -> return 0
def compare(v1, v2) -> int:
    if type(v1) is int and type(v2) is int:
        return v1 - v2
    elif type(v1) is list and type(v2) is list:
        for i in range(min(len(v1), len(v2))):
            if compare(v1[i], v2[i]) == 0:
                continue
            return compare(v1[i], v2[i])
        if len(v1) < len(v2):
            return -1
        elif len(v1) == len(v2):
            return 0
        else:
            return 1
    elif type(v1) is list and type(v2) is int:
        return compare(v1, [v2])
    return compare([v1], v2)
        
        
            
def parse(s):
    return [eval(x) for x in s.split("\n") if x != ""]

def part2(filename):
    devider1, devider2 = [[2]], [[6]]
    packets = parse(open(filename).read()) + [devider1] + [devider2]
    
    #sort using selection sort
    for i in range(len(packets)):
        smallest = i
        for j in range(i + 1, len(packets)):
            if compare(packets[j], packets[smallest]) < 0:
                smallest = j
        packets[i], packets[smallest] = packets[smallest], packets[i]
    
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
main()