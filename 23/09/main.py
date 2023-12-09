import time
class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [[int(x) for x in line.split(" ")] for line in open(self.filename).read().split("\n")]
        
    def findTree(self, line):
        tree = [line]
        while True:
            current = tree[-1]
            diff = []
            for i in range(len(current) - 1):
                diff.append(current[i + 1] - current[i])
            tree.append(diff)
            z = False
            for d in diff:
                if d != 0:
                    z = True
            if not z:
                break
        return tree
        
            
    def solve(self, data):
        s = 0
        for line in data:
            tree = self.findTree(line)
            tree[-1].append(0)
            for i in range(len(tree) - 2, -1, -1):
                tree[i].append(tree[i + 1][-1] + tree[i][-1])  
            s += tree[0][-1]
        return s
        
    def part1(self):
        return self.solve(self.data)
    
    def part2(self):
        return self.solve([x[::-1] for x in self.data])
    
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