import re
class Solution():
    def __init__(self, test=False) -> None:
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.instructions = [self.parseLine(line) for line in open(self.filename).read().split("\n")]
        self.data = None
        self.commands = None
        
    def part1(self):
        self.data = [[False for _ in range(1000)] for _ in range(1000)]
        self.commands = {"turn on": lambda x : True, "turn off": lambda x : False, "toggle": lambda x : not x}
        self.runInstructions()
        
        result = 0
        for y in range(1000):
            for x in range(1000):
                if self.data[y][x]:
                    result += 1     
        return result

    
    def part2(self):
        self.data = [[0 for _ in range(1000)] for _ in range(1000)]
        self.commands = {"turn on": lambda x : x + 1, "turn off": lambda x : max(0, x - 1), "toggle": lambda x : x + 2}
        self.runInstructions()
        
        result = 0       
        for y in range(1000):
            for x in range(1000):
                result += self.data[y][x]
        return result
    
    def runInstructions(self):
        for instruction in self.instructions:
            command = self.commands[instruction[0]]
            x1 = instruction[1]
            y1 = instruction[2]
            x2 = instruction[3]
            y2 = instruction[4]
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    self.data[y][x] = command(self.data[y][x])
    

    #copied from https://github.com/runarmod/adventofcode/blob/main/2015/06/1/main.py
    def parseLine(self, line):
        line_re = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")
        match = line_re.match(line).groups() # command, x0, y0, x1, y1
        return match[0], *(int(match[i]) for i in range(1,5))
    
    
def main():
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
main()