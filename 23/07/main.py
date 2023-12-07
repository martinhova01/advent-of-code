import time

class Hand():
    def __init__(self, cards, bid, part2=False):
        self.cards = cards
        self.bid = bid
        self.cardTypes = ["A", "K","Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.type = self.findType(self.cards) if not part2 else self.findType2()
        self.part2 = part2
        
    def findType2(self):
        self.cardTypes = ["A", "K","Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
        
        count = {}
        for c in self.cards:
            if c not in count:
                count[c] = 0
            count[c] += 1
           
        mostFrequentNotJStr = "J"
        mostFrequentNotJ = 0
        for key, value in count.items():
            if key != "J" and value > mostFrequentNotJ:
                mostFrequentNotJ = value
                mostFrequentNotJStr = key
        
        bestCards = list(self.cards)
        for i in range(len(bestCards)):
            if bestCards[i] == "J":
                bestCards[i] = mostFrequentNotJStr
        
        return self.findType("".join(bestCards))
        
        
    def findType(self, cards):
        count = {}
        for c in cards:
            if c not in count:
                count[c] = 0
            count[c] += 1
        
        if 5 in count.values():
            return 0
        if 4 in count.values():
            return 1
        if 3 in count.values() and 2 in count.values():
            return 2
        if 3 in count.values():
            return 3
        pairs = 0
        for v in count.values():
            if v == 2:
                pairs += 1
        if pairs == 2:
            return 4
        if pairs == 1:
            return 5
        return 6
        
    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        
        for i in range(len(self.cards)):
            sCard = self.cards[i]
            oCard = other.cards[i]
            if sCard != oCard:
                return self.cardTypes.index(sCard) < self.cardTypes.index(oCard)
            
        return False
        
        
class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [Hand(line.split(" ")[0], int(line.split(" ")[1])) for line in open(self.filename).read().split("\n")]
        
        
    def part1(self):
        sortedhands = sorted(self.data)    
        s = 0
        for i in range(len(sortedhands), 0, -1):
            s += sortedhands[len(sortedhands) - i].bid * i
        return s
    
    def part2(self):
        self.data = [Hand(line.split(" ")[0], int(line.split(" ")[1]), part2=True) for line in open(self.filename).read().split("\n")]
        sortedhands = sorted(self.data)
        s = 0
        for i in range(len(sortedhands), 0, -1):
            s += sortedhands[len(sortedhands) - i].bid * i  
        return s
    
    
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