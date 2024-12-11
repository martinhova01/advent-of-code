import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [int(x) for x in open(self.filename).read().rstrip().split(" ")]
        
    def part1(self):
        for _ in range(25):
            new_data = []
            for stone in self.data:
                st = str(stone)
                if stone == 0:
                    new_data.append(1)
                    
                elif len(st) % 2 == 0:
                    s1 = int(st[: len(st) // 2])
                    s2 = int(st[len(st) // 2 :])
                    new_data.append(s1)
                    new_data.append(s2)
                else:
                    new_data.append(stone * 2024)
            self.data = new_data
        
        return len(self.data)
    
    def split(self, stone, depth):
        if (stone, depth) in self.memo:
            return self.memo[(stone, depth)]
        
        st = str(stone)
        res = None
        if depth == 75:
            return 1
        if stone == 0:
            res = self.split(1, depth + 1)
            
        elif len(st) % 2 == 0:
            s1 = int(st[: len(st) // 2])
            s2 = int(st[len(st) // 2 :])
            res = self.split(s1, depth + 1) + self.split(s2, depth + 1)
            
        else:
            res = self.split(stone * 2024, depth + 1)
            
        self.memo[(stone, depth)] = res
        return res
                
    
    def part2(self):
        self.data = [int(x) for x in open(self.filename).read().rstrip().split(" ")] # reset input
        self.memo = {}
        return sum(self.split(stone, 0) for stone in self.data)
    
    
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