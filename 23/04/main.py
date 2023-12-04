class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [self.parseLine(line) for line in open(self.filename).read().split("\n")]
        
    def parseLine(self, line):
        data = line.split(": ")[1]
        
        targetNums = []
        for x in data.split(" | ")[0].split(" "):
            if x != "":
                targetNums.append(int(x))
                
        drawnNums = []
        for x in data.split(" | ")[1].split(" "):
            if x != "":
                drawnNums.append(int(x))
                
        return {"targetNums": targetNums, "drawnNums": drawnNums}
        
    def part1(self):
        s = 0
        for i in range(len(self.data)):
            matches = self.getMatches(i)
            s += 2**(matches - 1) if matches > 0 else 0
        return s
    
    def part2(self):
        cards = [1 for _ in range(len(self.data))]
        for i in range(len(self.data)):
            matches = self.getMatches(i)
            for j in range(1, matches + 1):
                cards[i + j] += cards[i]
        return sum(cards)
            
    def getMatches(self, i):
        return len(set(self.data[i]["drawnNums"]).intersection(self.data[i]["targetNums"]))
    
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