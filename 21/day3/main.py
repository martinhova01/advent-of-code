def part1(inputfilename):
    with open(inputfilename) as f:
        lines = f.readlines()
        
        gamma = ""
        for i in range(len(lines[0]) - 1):
            bitlist = []
            
            for j in range(len(lines)):
                bitlist.append(lines[j][i])
            
            
            if bitlist.count("1") > bitlist.count("0"):
                gamma += "1"
            else:
                gamma += "0"
                
        epsilon = ""
        for char in gamma:
            if char == "1":
                epsilon += "0"
            else:
                epsilon += "1"
        
        return convertBinaryToDecimal(gamma) * convertBinaryToDecimal(epsilon)
        
        
        
def convertBinaryToDecimal(binary):
    exponent = len(binary) - 1
    result = 0
    
    for i in range(len(binary)):
        result += int(binary[i]) * (2 ** exponent)
        exponent -= 1
        
    return result
                        

def part2(inputfilename):
    with open(inputfilename) as f:
        numbers = f.readlines()
        
            #removing newline at the end of the numbers
        for i in range(len(numbers)):
            numbers[i] = numbers[i].strip()
        
        o2Level = convertBinaryToDecimal(findRating(numbers, True))
        co2Scrubbing = convertBinaryToDecimal(findRating(numbers, False))
        
        return o2Level * co2Scrubbing
            
            
def findMostCommonBit(numbers, pointer):
    counter1 = 0
    counter0 = 0
    
    for number in numbers:
        if number[pointer : pointer + 1] == "1":
            counter1 += 1
        else:
            counter0 += 1
            
    if counter1 < counter0:
        return "0"
    return "1"

def findRating(numbers, mostCommon):
    bitPointer = 0
    
    while len(numbers) > 1:
            criteria = findMostCommonBit(numbers, bitPointer)
            if not mostCommon:
                if criteria == "1":
                    criteria = "0"
                else:
                    criteria = "1"
                    
            newList = []
            for number in numbers:
                if number[bitPointer : bitPointer + 1] == criteria:
                    newList.append(number)
          
            numbers = newList
            bitPointer += 1
    
    return numbers[0]

def main(test = False):
    if test:
        filename = '21/day3/testinput.txt'
    else:
        filename = '21/day3/input.txt'
        
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
    
main()