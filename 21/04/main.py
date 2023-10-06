from Board import *

def parseInput(inputfilename):
    
    with open(inputfilename) as f:
        lines = f.readlines()
            #getting the drawn numbers and casting them to integers
        numbers = lines[0].split(",")
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i].strip())
            
        boards = []
        for boardNumber in range(2, len(lines), 6):
            newBoard = []
            for row in range(5):
                newRow = []
                for k in range(0, len(lines[boardNumber + row]), 3):
                    newRow.append(int(lines[boardNumber + row][k : k + 2]))
                newBoard.append(newRow)
            boards.append(Board(newBoard))
            
        return numbers, boards     
    
def part1(inputfilename):
    
    numbers, boards = parseInput(inputfilename)
    
    bingo = -1
    numberCounter = -1
    while bingo == -1:
        numberCounter += 1
        for i in range(len(boards)):
            boards[i].mark(numbers[numberCounter])
            if boards[i].hasBingo():
                bingo = i
                
    
    return boards[bingo].getSumOfUnmarkedNumbers() * numbers[numberCounter]
            
       
            
def part2(inputfilename):
    numbers, boards = parseInput(inputfilename)
    
    numberCounter = -1
    bingo = -1
    boardsWithBingo = []
    while True:
        numberCounter += 1
        for i in range(len(boards)):
            boards[i].mark(numbers[numberCounter])
            if boards[i].hasBingo() and boards[i] not in boardsWithBingo:
                bingo = i
                boardsWithBingo.append(boards[i])
            
                
        numberOfBingoes = 0
        for i in range(len(boards)):
            if boards[i].hasBingo():
                numberOfBingoes += 1
        if numberOfBingoes == len(boards):
            break
        
    return boards[bingo].getSumOfUnmarkedNumbers() * numbers[numberCounter]
            
            

def main(test = False):
    filename = "testinput.txt" if test else "input.txt"  
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
    
main()