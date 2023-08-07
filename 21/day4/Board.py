class Board:
    
    def __init__(self, board):
        self.board = board
        self.marked = [[False for x in range(5)] for x in range(5)] #False means not marked and true means marked
        
    def hasBingo(self):
        for row in range(len(self.board)):
            counter = 0
            while self.marked[row][counter]:
                counter += 1
                if counter == 5:
                    return True
                
        for col in range(len(self.board[0])):
            counter = 0
            while self.marked[counter][col]:
                counter += 1
                if counter == 5:
                    return True
        
        return False
    
    def mark(self, number):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == number:
                    self.marked[i][j] = True
                    return
                
    # def mark(self, row, col):
    #     self.marked[row][col] = True
        
    def getBoard(self):
        return self.board
    
    def getMarked(self):
        return self.marked
    
    def getSumOfUnmarkedNumbers(self):
        sum = 0
        for i in range(5):
            for j in range(5):
                if not self.marked[i][j]:
                    sum += self.board[i][j]
        return sum
    