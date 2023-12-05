class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.seeds, self.data = self.parse() #used in part 1
        self.seedRanges = self.parseSeeds() # used in part 2
        self.ranges = [[{"from": range(x[1], x[1] + x[2]), "to": range(x[0], x[0] + x[2])} for x in dataline]for dataline in self.data] # used in part 2
        
    def parseSeeds(self):
        sections = open(self.filename).read().split("\n\n")
        seeds = [int(x) for x in sections[0].split(": ")[1].split(" ")]
        seedRanges = []
        for i in range(0, len(seeds), 2):
            seedRanges.append(range(seeds[i], seeds[i] + seeds[i + 1]))
        return seedRanges
        
    def parse(self):
        sections = open(self.filename).read().split("\n\n")
        seeds = [int(x) for x in sections[0].split(": ")[1].split(" ")]
        
        data = []
        for i in range(1, len(sections)):
            section = []
            for line in sections[i].split("\n"):
                if not line[0].isdigit():
                    continue
                destStart = int(line.split(" ")[0])
                sourceStart = int(line.split(" ")[1])
                length = int(line.split(" ")[2])
                dataLine = [destStart, sourceStart, length]
                section.append(dataLine)
            data.append(section)
        
        return seeds, data
                   
    def part1(self):
        locations = []
        for seed in self.seeds:
            n = seed
            for i in range(len(self.data)):
                n = self.mapNumber(n, i)
            locations.append(n)
        return min(locations)
    
    def mapNumber(self, n, i):
        nextN = n
        section = self.data[i]
        for line in section:
            if line[1] <= n <= line[1] + line[2]:
                offset = n - line[1]
                nextN = line[0] + offset
                break
        return nextN
    
    def part2(self):
            #for each mapping
        for i in range(len(self.ranges)):
            new_seedRanges = []
                #for each seed range
            for seedRange in self.seedRanges:
                    #for each line in mapping
                for m in self.ranges[i]:
                    fr = m["from"]
                    tr = m["to"]
                    offset = tr.start - fr.start
                        #check if seedRange is in the fromRange
                    if seedRange.stop <= fr.start or fr.stop <= seedRange.start:
                        continue
                    ir = range(max(seedRange.start, fr.start), min(seedRange.stop, fr.stop))
                    lr = range(seedRange.start, ir.start)
                    rr = range(ir.stop, seedRange.stop)
                        #add what is left on left of range
                    if lr:
                        self.seedRanges.append(lr)
                        #add what is left on right of range
                    if rr:
                        self.seedRanges.append(rr)
                    new_seedRanges.append(range(ir.start + offset, ir.stop + offset))
                    break
                else:
                    #there was no mapping for this range
                    new_seedRanges.append(seedRange)
            self.seedRanges = new_seedRanges
            
        return min(x.start for x in self.seedRanges)
    
    
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