import hashlib
class Solution():
    def __init__(self) -> None:
        self.data = "ckczppom"
        
        
    def part1(self):
        return self.run(5)
    
    def part2(self):
        return self.run(6)
    
    def run(self, number_of_0s):
        i = 0
        while True:
            data = self.data + str(i)
            h = self.getHashedString(data)
            if h[:number_of_0s] == "0" * number_of_0s:
                return i
            i+=1
        
    def getHashedString(self, data):
        hasher = hashlib.md5()
        hasher.update(data.encode("utf-8"))
        return str(hasher.hexdigest())
    
def main():
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
main()