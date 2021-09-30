

class Solution:
    
    def checker(self, s,l,r): 
       while l >= 0 and r < len(s) and s[l] == s[r]:
          l -= 1
          r += 1
     	 
       return s[l+1:r]
     
    def longest_palindromic(self, s: str) -> str:
        maximum = " "
        for i in range(len(s)):
             case_1 = self.checker(s, i, i)
             if len(case_1) > len(maximum):
              	maximum = case_1
             case_2 = self.checker(s, i, i+1) 
             if len(case_2) > len(maximum): 
                  maximum = case_2 
        return maximum



p = Solution()
print(p.longest_palindromic("cbbd"))
