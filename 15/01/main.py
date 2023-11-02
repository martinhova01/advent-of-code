class Solution():
    def __init__(self, test=False) -> None:
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read()
        
    def part1(self):
        floor = 0
        for c in self.data:
            floor += 1 if c == "(" else -1
        return floor
    
    def part2(self):
        floor = 0
        for i in range(len(self.data)):
            floor += 1 if self.data[i] == "(" else -1
            if floor == -1:
                return i + 1
    
    
def main():
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
main()