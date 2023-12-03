class Number():
    def __init__(self, line, start, end, value):
        self.line = line
        self.startPos = start
        self.endPos = end
        self.value = value
        self.neighborPositions = set()
        
class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [line for line in open(self.filename).read().split("\n")]
        self.numbers = set()
        self.directions = {(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)}
        self.findNumbers()
        
    def part1(self):
        s = 0
        for n in self.numbers:
            for (x, y) in n.neighborPositions:
                if not self.data[y][x].isdigit() and self.data[y][x] != ".":
                    s += n.value    
        return s             
    
    def part2(self):
        result = 0
        for i in range(len(self.data)):
            line = self.data[i]
            for j in range(len(self.data[i])):
                if line[j] == "*":
                    gearRatio = self.checkGear(i, j)
                    result += gearRatio        
        return result
    
    def checkGear(self, i, j):
        adjacentNumbers = set()
        for number in self.numbers:
            if (j, i) in number.neighborPositions:
                adjacentNumbers.add(number)
        return adjacentNumbers.pop().value * adjacentNumbers.pop().value if len(adjacentNumbers) == 2 else 0
        
    def findNumbers(self):
        for i in range(len(self.data)):
            j = 0
            while j < len(self.data[i]):
                if self.data[i][j].isdigit():
                    n = Number(i, j, -1, "")
                    value = ""
                    while self.data[i][j].isdigit():
                        value += self.data[i][j]
                        for (x, y) in self.directions:
                            if i + y < 0 or i + y >= len(self.data) or j + x < 0 or j + x >= len(self.data[i]):
                                continue
                            n.neighborPositions.add((j + x, i + y))
                        j += 1
                        if j == len(self.data[i]):
                            break
                    n.endPos = j - 1
                    n.value = int(value)
                    self.numbers.add(n)
                else:
                    j += 1
                                   
        
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