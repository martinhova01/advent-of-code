class Solution():
    def __init__(self, test=False) -> None:
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().split("\n")
        self.illegal = {"ab", "cd", "pq", "xy"}
        self.vowels = "aeiou"
        
    def part1(self):
        result = 0
        for s in self.data:
            vowels = 0
            double = False
            for i in range(len(s)):
                c = s[i]
                if c in self.vowels:
                    vowels += 1
                if i > 0:
                    if c == s[i - 1]:
                        double = True
                
            if vowels < 3 or not double:
                continue
            illegal = False
            for substring in self.illegal:
                if substring in s:
                    illegal = True
                    break
            result += 1 if not illegal else 0
            
        return result
        
                
            
    
    def part2(self):
        result = 0
        for s in self.data:
            reapeted_letter = False
            pair_indecies = {}
            for i in range(1, len(s)):
                
                if i < len(s) - 1:
                    if s[i - 1] == s[i + 1]:
                        reapeted_letter = True
                        
                pair = s[i-1:i+1]
                if pair not in pair_indecies:
                    pair_indecies[pair] = []
                pair_indecies[pair].append(i)
                
            if not reapeted_letter:
                continue
            
            overlap = True
            for pair, indecies in pair_indecies.items():
                if len(indecies) > 1:
                    for i in range(len(indecies)):
                        for j in range(i + 1, len(indecies)):
                            if abs(indecies[i] - indecies[j]) != 1:
                                overlap = False
            if not overlap:
                result += 1
        return result
                    
    
    
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