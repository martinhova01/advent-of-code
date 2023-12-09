from collections import defaultdict


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
    s = open(filename).read().split("\n\n")[0]
    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in open(filename).read().split("\n\n")[1].split("\n")}
    
    pair_map = {}
    for key, val in rules.items():
        pair_map[key] = (key[0] + val, val + key[1])
       
        #count all pairs
    pair_counts = defaultdict(int)
    for i in range(len(s) - 1):
        pair = s[i: i + 2]
        if  pair not in pair_counts:
            pair_counts[pair] = 0
        pair_counts[pair] += 1
        
        #run 40 steps
    for _  in range(40):
        new_pair_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            new_pair_counts[pair_map[pair][0]] += count
            new_pair_counts[pair_map[pair][1]] += count
        pair_counts = new_pair_counts
        
        #count characters in result
    c_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        c_counts[pair[0]] += count
        
    c_counts[s[-1]] += 1 #the last character is not counted
    
    countsList = sorted(c_counts.items(), key= lambda x : x[1])
    return (countsList[-1][1] - (countsList[0][1]))
        

def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
main()