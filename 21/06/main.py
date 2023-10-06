def part1(inputfilename):
    with open(inputfilename) as f:
            #parse input and cast to ints
        data = f.readline().split(",")
        for i in range(len(data)):
            data[i] = int(data[i])
            
    for i in range(80):
        numberOfFish = len(data)
        for j in range(numberOfFish):
            if data[j] == 0:
                data[j] = 6
                data.append(8)
            else:
                data[j] = data[j] - 1
    
    return len(data)

def part2(inputfilename):
    
    data = open(inputfilename).readline().split(",")
    
    fishCounts = [0] * 9
    for fish in data:
        fishCounts[int(fish)] += 1
        
    for _ in range(256):
        resets = fishCounts.pop(0)
        fishCounts.append(resets)
        fishCounts[6] += resets
        
    return sum(fishCounts)
     
     
def main(test = False):
    filename = "testinput.txt" if test else "input.txt"     
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
    
main()