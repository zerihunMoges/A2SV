class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        elif n == -1:
            return 1/x
        
        else:
             if n%2 == 0: 
                result = self.myPow(x,n//2)
                return result*result
             else:
                result = self.myPow(x,n//2)
                return result*result*x
            
