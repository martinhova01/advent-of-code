import copy
import time
import itertools as it
import re


class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [int(re.findall(r"\d", line)[1]) for line in open(self.filename).read().split("\n")]
        self.memo = {}
        
    def part1(self):
        dice = 0
        rolls = 0
        pos = [self.data[0] - 1, self.data[1] - 1]
        score = [0, 0]
        while True:
            for i in range(2):
                move = 0
                for _ in range(3):
                    dice += 1
                    if dice > 100:
                        dice = 1
                    move += dice
                    rolls += 1
                pos[i] = (pos[i] + move) % 10
                score[i] += pos[i] + 1
                if score[i] >= 1000:
                    return score[(i + 1) % 2] * rolls
    
    def part2(self):
        return max(self.sim([0, 0], [self.data[0] - 1, self.data[1] - 1], 0, 21))
    
    def sim(self, score: list[int], pos: list[int], turn, limit):
        """simulate a round of the game at a given state

        Args:
            score (list[int]): [player1, player2]
            pos (list[int]): [player1, player2]
            turn (int): 0 if player 1s turn, 1 if player 2s turn
            limit (int): the score-limit to win the game
        """
        if score[0] >= limit:
            return [1, 0]
        if score[1] >= limit:
            return [0, 1]
        
        wins = [0, 0]
        for dice_rolls in it.product((1, 2, 3), repeat=3):
            move = sum(dice_rolls)
            new_pos = copy.deepcopy(pos)
            new_score = copy.deepcopy(score)
            new_pos[turn] = (new_pos[turn] + move) % 10
            new_score[turn] += new_pos[turn] + 1
            
            hashable = (tuple(new_score), tuple(new_pos), (turn + 1) % 2)
            if hashable not in self.memo:
                self.memo[hashable] = self.sim(new_score, new_pos, (turn + 1) % 2, limit)
            res = self.memo[hashable]
            wins = [wins[x] + res[x] for x in range(2)]
        return wins
            
    
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