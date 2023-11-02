class Solution():
    def __init__(self, test=False) -> None:
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [tuple(int(x) for x in line.split("x")) for line in open(self.filename).read().split("\n")]
        
    def part1(self):
        sum = 0
        for (l, w, h) in self.data:
            sum += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
        return sum
    
    def part2(self):
        sum = 0
        for (l, w, h) in self.data:
            sum += min(2*l + 2*w, 2*w + 2*h, 2*h + 2*l) + (l*h*w)
        return sum
    
    
def main():
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
main()