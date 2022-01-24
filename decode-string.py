from curses.ascii import isdigit

class Solution:
    def decode(self, s, i, brackets, repeat):
        if i >= len(s):
            return s
        elif isdigit(s[i]):
            j = s.index('[', i)
            digit = ''.join(s[i:j])
            repeat.append(int(digit))
            s[i:j] = []
            brackets.append(i)
            return self.decode(s, i+1,brackets, repeat)
        
        elif len(brackets) == 0:
            return self.decode(s, i+1,brackets, repeat)
        
        elif s[i] == ']':
            
            j = brackets.pop(-1)
            r = repeat.pop(-1)
            s[j:i+1] =  r* s[j+1:i]
            return self.decode(s, j+ (r)*(i-j-1),brackets, repeat)
        
        return self.decode(s, i+1,brackets, repeat)

    
    def decodeString(self, s: str) -> str:
        decoded = ''
        bracket =[]
        repeat = []
        return ''.join(self.decode(list(s), 0, bracket, repeat))
        
