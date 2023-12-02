class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [self.parseLine(line) for line in open(self.filename).read().split("\n")]
        self.limits = {"red": 12, "green": 13, "blue": 14}
        
    def part1(self):
        return sum(i + 1 if self.isPossible(i) else 0 for i in range(len(self.data)))
    
    def isPossible(self, i):
        return self.data[i]["red"] <= self.limits["red"] \
            and self.data[i]["green"] <= self.limits["green"] \
            and self.data[i]["blue"] <= self.limits["blue"]
    
    def part2(self):
        return sum(game["red"] * game["green"] * game["blue"] for game in self.data)
    
    def parseLine(self, line):
        line = line.split(": ")[1]
        chunks = line.split("; ")
        res = {"red": 0, "green": 0, "blue": 0}
        for chunk in chunks:
            datapairs = chunk.split(", ")
            for datapair in datapairs:
                color = datapair.split(" ")[1]
                number = int(datapair.split(" ")[0])
                res[color] = max(res[color], number)  
        return res
                
    
def main():
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
main()