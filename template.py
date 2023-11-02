class Solution():
    def __init__(self, test=False) -> None:
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = None
        
    def part1(self):
        return -1
    
    def part2(self):
        return -1
    
    
def main():
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 1: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 1: {s.part2()}")
    
main()