import time
from collections import defaultdict

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().strip().split("\n")
        self.snafu_to_dec = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
        self.dec_to_snafu = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}
        
    def snafu_to_decimal(self, snafu: str) -> int:
        return sum(self.snafu_to_dec[snafu[i]] * (5**(len(snafu) - 1 - i)) for i in range(len(snafu)))
    
    def decimal_to_snafu(self, n: int) -> str:
        number_per_index = defaultdict(int)
        largest_index = 0
        while True:
            if n // (5 ** largest_index) == 0:
                break
            largest_index += 1
        largest_index -= 1
        
        for j in range(largest_index, -1, -1):
            number_per_index[j] = n // (5 ** j)
            n = n % (5 ** j)
        
        for i in range(largest_index + 1):
            if number_per_index[i] > 2:
                number_per_index[i + 1] += 1
                number_per_index[i] -= 5
        
        res = ""
        for i in range(largest_index, -1, -1):
            res += self.dec_to_snafu[number_per_index[i]]
        return res
            
    def part1(self):
        return self.decimal_to_snafu(sum(self.snafu_to_decimal(snafu) for snafu in self.data))
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()