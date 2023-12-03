class Solution():
    def __init__(self, test=False) -> None:
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().split("\n")
        self.numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        
    def part1(self):
        result = 0
        for line in self.data:
            left = -1
            right = -1 
            for i in range(len(line)):
                if line[i].isdigit():
                    left = line[i]
                    break
                    
            for i in range(len(line) - 1, -1, -1):
                if line[i].isdigit():
                    right = line[i]
                    break
            result += int(left + right)  
        return result
            
    
    def part2(self):
        result = 0
        for line in self.data:
            left = ""
            right = ""
            for i in range(len(line)):
                if left != "":
                    break
                if line[i].isdigit():
                    left = line[i]
                    break
                else:
                    for number in self.numbers:
                        if line[i:].startswith(number):
                            left = str(self.numbers.index(number) + 1)
                            break
                        
            for i in range(len(line) - 1, -1, -1):
                if right != "":
                    break
                if line[i].isdigit():
                    right = line[i]
                    break
                else:
                    for number in self.numbers:
                        if line[:i + 1].endswith(number):
                            right = str(self.numbers.index(number) + 1)
                            break
            result += int(left + right)
            
        return result
    
    
def main():
    s = Solution(test=True)
    print("---TEST---")
    # print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
main()