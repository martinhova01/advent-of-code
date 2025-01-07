import time


def mix(secret_num, value):
    return secret_num ^ value

def prune(secret_num):
    return secret_num % 16777216

def next_secret_num(secret_num):
    res = prune(mix(secret_num, secret_num * 64))
    res = prune(mix(res, res // 32))
    res = prune(mix(res, res * 2048))
    return res

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [int(line) for line in open(self.filename).read().rstrip().split("\n")]
        
    def part1(self):
        s = 0
        for num in self.data:
            for _ in range(2000):
                num = next_secret_num(num)
            s += num
        return s
    
    def part2(self):
        return None
    
    
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