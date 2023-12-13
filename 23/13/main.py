import time
class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.blocks = [x for x in open(self.filename).read().split("\n\n")]
        self.part1Solutions = []
        
    def findHorizontalLine(self, block, blockNum):
        lines = block.split("\n")
        for i in range(len(lines) - 1):
            if lines[i] == lines[i + 1]:
                j = 1
                while i - j + 1 >= 0 and i + j < len(lines):
                    if lines[i - j + 1] == lines[i + j]:
                        j += 1
                    else:
                        j = 1
                        break
                if j != 1:
                    if len(self.part1Solutions) - 1 < blockNum:
                        self.part1Solutions.append(("h", i + 1))
                    elif self.part1Solutions[blockNum] == ("h", i + 1):
                        continue
                    return i + 1 
                
                
        return 0
    
    
    def findVerticalLine(self, block, blockNum):
        lines = block.split("\n")
                
        for i in range(len(lines[0]) - 1):
            if all(line[i] == line[i + 1] for line in lines):
                j = 1
                while i - j + 1 >= 0 and i + j < len(lines[0]):
                    if all(line[i - j + 1] == line[i + j] for line in lines):
                        j += 1
                    else:
                        j = 1
                        break
                if j != 1:
                    if len(self.part1Solutions) - 1 < blockNum:
                        self.part1Solutions.append(("v", i + 1))
                    elif self.part1Solutions[blockNum] == ("v", i + 1):
                        continue
                    return i + 1 
                
        return 0
    
            
    def part1(self):
        s = 0
        for i in range(len(self.blocks)):
            block = self.blocks[i]
            v = self.findVerticalLine(block, i)
            h = self.findHorizontalLine(block, i)
            if v != 0:
                s += v
            else:
                s += h * 100 
        return s
    
    
    def part2(self):
        s = 0
        for i in range(len(self.blocks)):
            block = self.blocks[i]
            for j in range(len(block)):
                if block[j] == "\n":
                    continue
                elif block[j] == "#":
                    newBlock = block[:j] + "." + block[j + 1:]
                else:
                    newBlock = block[:j] + "#" + block[j + 1:]
                    
                v = self.findVerticalLine(newBlock, i)
                h = self.findHorizontalLine(newBlock, i)
                
                if v != 0:
                    s += v
                    break
                elif h != 0:
                    s += h * 100
                    break       
        return s
                        
    
    
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