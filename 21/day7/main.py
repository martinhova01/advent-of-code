import math
class Crab:
    def __init__(self, pos):
        self.pos = pos
        
        
    def moveTo(self, newPos):
        return abs(self.pos - newPos)
    
    def getPos(self):
        return self.pos
    
    

def part1(inputfilename):
    crabs = []
    for crabPos in open(inputfilename).readline().split(","):
        crabs.append(Crab(int(crabPos)))
        
    highestPos = 0
    for crab in crabs:
        if crab.getPos() > highestPos:
            highestPos = crab.getPos()
            
    bestFuelUsage = math.inf
    for i in range(highestPos):
        fuelUsage = 0
        for crab in crabs:
            fuelUsage += crab.moveTo(i)
            
        if fuelUsage < bestFuelUsage:
            bestFuelUsage = fuelUsage
            
    return bestFuelUsage

def part2(inputfilename):
    return -1

def main(test = False):
    if test:
        filename = '21/day7/testinput.txt'
    else:
        filename = '21/day7/input.txt'
        
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
    
main()

