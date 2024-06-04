from collections import Counter

def part1(filename):
    lines = open(filename).read().split("\n")
    sum = 0
    targetSizes = [2, 3, 4, 7]
    for line in lines:
        data = line.split(" | ")[1].split(" ")
        for digit in data:
            size = len(digit)
            if size in targetSizes:
                sum += 1     
    return sum

def part2(filename):
    segments_to_digit = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    lines = open(filename).read().split("\n")
    result = 0
    for line in lines:
        digits, output = [x.split(" ") for x in line.split(" | ")]
        segment_mapping = {}
        digits = [set(x) for x in digits]
        digits.sort(key=lambda x: len(x))
        
        used_segments = set()
        #a
        a_mapping = list(digits[1].difference(digits[0]))[0]
        segment_mapping["a"] = a_mapping
        used_segments.add(a_mapping)
        
        #b, e, f
        c = Counter()
        for digit in digits:
            for segment in digit:
                c[segment] += 1
        for segment, count in c.items():
            if count == 9:
                segment_mapping["f"] = segment
                used_segments.add(segment)
            elif count == 6:
                segment_mapping["b"] = segment
                used_segments.add(segment)
            elif count == 4:
                segment_mapping["e"] = segment
                used_segments.add(segment)
        
        #c
        c_mapping = list(digits[0].difference(used_segments))[0]
        used_segments.add(c_mapping)
        segment_mapping["c"] = c_mapping
        
        #d
        d_mapping = list(digits[2].difference(used_segments))[0]
        used_segments.add(d_mapping)
        segment_mapping["d"] = d_mapping
        
        #g
        segment_mapping["g"] = list(digits[6].difference(used_segments))[0]
        
        #invert mapping dict
        new_segment_mapping = {}
        for key, value in segment_mapping.items():
            new_segment_mapping[value] = key
        segment_mapping = new_segment_mapping
        
        number = ""
        for digit in output:
            segments = ""
            for c in digit:
                segments += segment_mapping[c]
            segments = "".join(sorted(segments))
            number += str(segments_to_digit.index(segments))
        
        result += int(number, 10)
    
    return result
        
        
        
    
def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
main()