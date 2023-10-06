from collections import deque
from pathlib import Path
validPairs = {"(": ")", "{": "}", "[": "]", "<": ">"}
def part1(filename):
    data = [x for x in open(filename).read().split("\n")]
    incompleteLines = list(data)
    
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    
    result = 0
    for s in data:
        stack = deque()

        for i in range(len(s)):
            c = s[i]
            if c in validPairs:
                stack.append(c)
            else:
                topElem = stack.pop()
                if c != validPairs[topElem]:
                    result += scores[c]
                    incompleteLines.remove(s)
                    break
    return (result, incompleteLines)

        


def part2(filename):
    
    incompleteLines = part1(filename)[1]
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    
    lineScores = []
    for s in incompleteLines:
        stack = deque()

        for i in range(len(s)):
            c = s[i]
            if c in validPairs:
                stack.append(c)
            else:
                stack.pop()
                
        completionString = ""
        while stack:
            completionString += validPairs[stack.pop()]
            
        score = 0
        for c in completionString:
            score = 5 * score + scores[c]
        lineScores.append(score)
        
    lineScores.sort()
    return lineScores[(len(lineScores) // 2)]
            
    
def main(test = False):
    if test:
        filename = str(Path(__file__).parent / "testinput.txt")
    else:
        filename = str(Path(__file__).parent / "input.txt")
        
    print(f"part 1 : {part1(filename)[0]}")
    print(f"part 2 : {part2(filename)}")
    
main()