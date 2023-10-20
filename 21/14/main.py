def part1(filename):
    s = open(filename).read().split("\n\n")[0]
    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in open(filename).read().split("\n\n")[1].split("\n")}
    
    for _ in range(10):
        newS = s[0]
        for i in range(len(s) - 1):
            pair = s[i : i + 2]
            if pair in rules:
                newS += rules[pair] + pair[1]
        s = newS
        
    counts = {}
    for c in s:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
        
    countsList = sorted(counts.items(), key= lambda x : x[1])
    return (countsList[-1][1] - countsList[0][1])
            


def part2(filename):
    pass




def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
main()