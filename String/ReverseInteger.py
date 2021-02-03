class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            if x < 0:
                sign = "-"
                limit = str(2**31-1)
                limit = limit[:-1] + "8"
            else:
                sign = ""
                limit = str(2**31-1)
            #remove last 0
            while x%10 == 0:
                x/=10
            xx = str(int(abs(x)))
            answer = ""
            isSmaller = False
            if len(xx) == len(limit):
                for i in range(len(xx)):
                    if xx[-1-i] > limit[i] and not isSmaller:
                        return 0
                    if xx[-1-i] < limit[i]:
                        isSmaller = True
                    answer +=  xx[-1-i]
                
            else:
                for i in range(len(xx)):
                    answer += xx[-1-i]
                    
            return int(sign + answer)
