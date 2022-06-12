class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        
        for i in range(n//2):
            s[i], s[n-i -1] = s[n-i-1], s[i]
            
        return s
        
class Solution:
  def reverseString(self, s: List[str], i=0) -> None:
      """
      Do not return anything, modify s in-place instead.
      """
      # base case
      if i >= len(s)//2:
          return 
      s[i], s[len(s) - i - 1] =  s[len(s) - i - 1], s[i]
      return self.reverseString(s, i+1)
