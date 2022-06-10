class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cell = [0, 0]
        
        for move in moves:
            if move == 'U':
                cell[0] -= 1
            elif move == 'D':
                cell[0] += 1
            elif move == 'L':
                cell[1] -= 1
            elif move == 'R':
                cell[1] +=1
        return cell == [0, 0]
        
