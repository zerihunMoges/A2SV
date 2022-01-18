class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        result = n/3
        if result == 3 or n==1:
            return True
        
        elif result < 3 and result != 1 :
            return False
        
        else:
            return self.isPowerOfThree(result)
