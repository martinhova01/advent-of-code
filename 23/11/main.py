import time
class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [[x for x in line] for line in open(self.filename).read().split("\n")]
    
    def solve(self, expansions):
        rowsToExpand = []
        for row in range(len(self.data)):
            if all(self.data[row][col] == "." for col in range(len(self.data[row]))):
                rowsToExpand.append(row)
              
        colsToExpand = []
        for col in range(len(self.data[0])):
            if all(self.data[row][col] == "." for row in range(len(self.data))):
                colsToExpand.append(col)
                
        nodes = []
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "#":
                    nodes.append((x, y))

        s = 0
        for i in range(len(nodes)):
            u = nodes[i]
            for j in range(i + 1, len(nodes)):
                v = nodes[j]
                crossed = 0
                for row in rowsToExpand:
                    if row in range(min(u[1], v[1]), max(u[1], v[1])):
                        crossed += 1
                for col in colsToExpand:
                    if col in range(min(u[0], v[0]), max(u[0], v[0])):
                        crossed += 1       
                
                dist = abs(u[0] - v[0]) + abs(u[1] - v[1]) + crossed * (expansions - 1)
                s += dist
                
        return s
    
    def part1(self):
        return self.solve(2)
    
    def part2(self):
        return self.solve(1000000)
    
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