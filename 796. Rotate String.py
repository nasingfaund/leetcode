class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == "" and goal == "":
            return True

        for i in range(len(s)):
            if goal == s:
                return True
            s = s[1:] + s[0]

        return False

