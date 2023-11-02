class Solution():
    def __init__(self, test=False) -> None:
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read()
        self.directions = {"<": (-1, 0), "^": (0, 1), ">": (1, 0), "v": (0, -1)}
        
    def part1(self):
        x, y = 0, 0
        visited = set()
        visited.add((x, y))
        for c in self.data:
            x += self.directions[c][0]
            y += self.directions[c][1]
            visited.add((x, y))
        return len(visited)
    
    def part2(self):
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        visited = set()
        visited.add((0, 0))
        for i in range(len(self.data)):
            c = self.data[i]
            if i % 2 == 0:
                x1 += self.directions[c][0]
                y1 += self.directions[c][1]
                visited.add((x1, y1))
            else:
                x2 += self.directions[c][0]
                y2 += self.directions[c][1]
                visited.add((x2, y2)) 
        return len(visited)
    
    
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