from collections import Counter
from itertools import product
import time
from tqdm import tqdm


def generateCombinations(k) -> list[str]:
    return [''.join(combination) for combination in product(["#", "."], repeat=k)]

def isValidString(s, groups) -> bool:
    counts = Counter(s)
    if counts["#"] != sum(groups):
        return False
    
    blocks = [block for block in s.split(".") if block != ""] 
    for i in range(len(blocks)):
        if len(blocks[i]) != groups[i]:
            return False
    return True
    
    
def possibleCombs(s, groups) -> int:
    counts = Counter(s)
    combs = generateCombinations(counts["?"])
    
    sum = 0
    for comb in combs:
        newS = s
        for c in comb:
            newS = newS.replace("?", c, 1)
        if isValidString(newS, groups):
            sum += 1
            
    return sum

    
class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [line for line in open(self.filename).readlines()]
        self.springs = [line.split(" ")[0] for line in self.data]
        self.groups = [eval(f"[{line.split(" ")[1]}]") for line in self.data]
        self.memo = {}
        
        #brute force!!
    def part1(self):
        s = 0
        for i in tqdm(range(len(self.springs))):
            s+= possibleCombs(self.springs[i], self.groups[i])
        return s
    
    def part2(self):
        newSprings = []
        newGroups = []
        for i in range(len(self.springs)):
            newSprings.append(self.springs[i] + ("?" + self.springs[i]) * 4)
            newGroup = []
            for _ in range(5):
                for x in self.groups[i]:
                    newGroup.append(x)
            newGroups.append(newGroup)
            
        s = 0
        for i in tqdm(range(len(newSprings))):
            string = newSprings[i]
            groups = newGroups[i]
            s += self.solve(string, groups)
            
        return s
    
    def solve(self, string, groups):
        blockLength = groups[0]
            #base case -> only one block to place
        if len(groups) == 1:
            s = 0
            for i in range(len(string) - blockLength + 1):
                if all(c != "." for c in string[i:i+ blockLength]):
                    newString = string[:i ] + "#" * blockLength + string[i+blockLength:]
                    newString = newString.replace("?", ".")
                    if not self.isValidPlacement(newString, blockLength):
                        continue
                    count = Counter(newString)
                    if count["#"] != blockLength:
                        continue
                    s += 1
                    
            return s
                
                
            #other case -> try all valid placements for groups[0] and solve the rest recursivly
        else:
            if (string, tuple(groups)) in self.memo:
                return self.memo[(string, tuple(groups))]
            s = 0
            if "#" in string:
                firstHashtag = string.index("#")
            else:
                firstHashtag = -1
            for i in range(firstHashtag + 1 if firstHashtag != -1 else len(string) - blockLength + 1):
                if all(c != "." for c in string[i:i+ blockLength]):
                    newString = string[:i ] + "#" * blockLength + string[i+blockLength:]
                    newStringTest = newString.replace("?", ".")
                    if not self.isValidPlacement(newStringTest, blockLength):
                        continue
                    
                    s += self.solve(string[i + blockLength + 1:], groups[1:])
                    
            self.memo[(string, tuple(groups))] = s
            return s
        
        
    def isValidPlacement(self, string, blockLength):
        blocks = [block for block in string.split(".") if block != ""] 
        return len(blocks[0]) == blockLength
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()