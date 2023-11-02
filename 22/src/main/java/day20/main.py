
def part1(filename):
    data = [Integer(int(x)) for x in open(filename).read().split("\n")]
    result = list(data)
    
    mix(data, result)
    
    return findCoordinates(result)
        
    
def part2(filename):
    key = 811589153
    data = [Integer(int(x) * key) for x in open(filename).read().split("\n")]
    result = list(data)
    
    for _ in range(10):
        mix(data, result)
    
    return findCoordinates(result)
    
        
def findCoordinates(l):
    index_of_0 = -1
    for i in range(len(l)):
        if l[i].steps == 0:
            index_of_0 = i
    sum = 0
    for i in range(1000, 3001, 1000):
        sum += l[(index_of_0 + i) % len(l)].steps
    return sum


def mix(orgList, currentList):
    for x in orgList:
        old_index = currentList.index(x)
        new_index = (old_index + x.steps) % (len(orgList) - 1)
        currentList.insert(new_index, currentList.pop(old_index))
        
        
class Integer():
    def __init__(self, steps) -> None:
        self.steps = steps


def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
    
main()