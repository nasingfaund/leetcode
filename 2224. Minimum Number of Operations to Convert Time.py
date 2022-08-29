class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        minutes = [60, 15, 5, 1]
        counter = 0
        current_hour, current_minutes = map(int, current.split(":"))
        current = current_hour * 60 + current_minutes
        
        correct_hour, correct_minutes = map(int, correct.split(":"))
        correct = correct_hour * 60 + correct_minutes
        
        if current == correct:
            return counter
        
        i = 0
        while i < len(minutes):
            if current + minutes[i] <= correct:
                current += minutes[i]
                counter += 1
            else:
                i+=1

            if current ==  correct:
                return counter

            
        
        
