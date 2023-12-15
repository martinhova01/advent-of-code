import time
from collections import defaultdict

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [x for x in open(self.filename).read().split(",")]
        self.hashmap = defaultdict(int)
        
    def hashString(self, s):
        val = 0
        for c in s:
            val += ord(c)
            val *= 17
            val %= 256
        return val
        
    def part1(self):
        s = 0
        for string in self.data:
            s += self.hashString(string)
        return s
    
    def part2(self):
        instructions = [self.parseInstruction(instruction) for instruction in self.data]
        for instruction in instructions:
            operator = instruction[0]
            label = instruction[1]
            index = self.hashString(label)
            if operator == "=":
                if index not in self.hashmap:
                    self.hashmap[index] = []
                listIndex = self.findListIndex(self.hashmap[index], label)
                if listIndex == -1:
                    self.hashmap[index].append((label, instruction[2]))
                else:
                    self.hashmap[index][listIndex] = (label, instruction[2])
            else:
                if index not in self.hashmap:
                    continue
                listIndex = self.findListIndex(self.hashmap[index], label)
                if listIndex != -1:
                    self.hashmap[index].pop(listIndex)
                
        return self.calculateFocusPower()
    
    def findListIndex(self, l, label):
            for i in range(len(l)):
                if l[i][0] == label:
                    return i
            return -1
        
    def calculateFocusPower(self):
        s = 0
        for i in self.hashmap.keys():
            for j in range(len(self.hashmap[i])):
                s += (1 + i) * (1 + j) * self.hashmap[i][j][1]   
        return s
                
    
    def parseInstruction(self, instruction):
        if "-" in instruction:
            return ("-", instruction[: len(instruction) - 1])
        return ("=", instruction.split("=")[0], int(instruction.split("=")[1]))
    
    
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