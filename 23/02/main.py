class Solution():
    def __init__(self, test=False) -> None:
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [self.parseLine(line) for line in open(self.filename).read().split("\n")]
        self.limits = {"red": 12, "green": 13, "blue": 14}
        
    def part1(self):
        ids = set()
        for i  in range(len(self.data)):
            game = self.data[i]
            if game["red"] <= self.limits["red"] and game["green"] <= self.limits["green"] and game["blue"] <= self.limits["blue"]:
                ids.add(i + 1)
        return sum(ids)
    
    def part2(self):
        res = 0
        for game in self.data:
            res += game["red"] * game["green"] * game["blue"]
        return res
    
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