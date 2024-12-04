import time
import copy

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [list(x) for x in open(self.filename).read().rstrip().split("\n")]
    
    
    def add_padding(self, length):
        text = copy.deepcopy(self.data)
        for y in range(len(text)):
            for _ in range(length):
                text[y].insert(0, ".")
                text[y].append(".")
        row = ["." for _ in range(len(text[0]))]
        for _ in range(length):
            text.insert(0, row)
            text.append(row)
        return text
        
        
    def part1(self):
        padding = 4
        N = len(self.data) + padding
        text = self.add_padding(padding)
        words = ["XMAS", "SAMX"]
        s = 0
        for word in words:
                        
            for y in range(padding, N):
                for x in range(padding, N):
                    if all(text[y + i][x + i] == word[i] for i in range(len(word))):
                        s += 1
                        
                    if all(text[y - i][x + i] == word[i] for i in range(len(word))):
                        s += 1
                        
                    if all(text[y + i][x] == word[i] for i in range(len(word))):
                        s += 1
                    
                    if all(text[y][(x + i)] == word[i] for i in range(len(word))):
                        s += 1   
        return s
    
    def part2(self):
        padding = 4
        N = len(self.data) + padding
        text = self.add_padding(padding)
        s = 0    
        for y in range(padding, N):
            for x in range(padding, N):
                if text[y][x] != "A":
                    continue
                if text[y + 1][x + 1] == "M" and text[y - 1][x - 1] == "S" and text[y + 1][x - 1] == "M" and text[y - 1][x + 1] == "S":
                    s += 1
                    
                if text[y + 1][x + 1] == "S" and text[y - 1][x - 1] == "M" and text[y + 1][x - 1] == "M" and text[y - 1][x + 1] == "S":
                    s += 1
                    
                if text[y + 1][x + 1] == "M" and text[y - 1][x - 1] == "S" and text[y + 1][x - 1] == "S" and text[y - 1][x + 1] == "M":
                    s += 1
                    
                if text[y + 1][x + 1] == "S" and text[y - 1][x - 1] == "M" and text[y + 1][x - 1] == "S" and text[y - 1][x + 1] == "M":
                    s += 1
                    
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