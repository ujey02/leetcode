class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        prob = self.rec(n-1,n-1,1)
        return ["(" + prev for prev in prob]
    
    def rec(self, p1, p2,isOpened):
        prob1, prob2 = [],[]
        if p1 == 0 and p2 == 0:
            return [")"]
        if p1 != 0:
            prob1 = self.rec(p1-1,p2,isOpened+1) 
            prob1 = ["(" + prev for prev in prob1]
        if p2 != 0 and isOpened > 0:
            prob2 = self.rec(p1,p2-1,isOpened-1)
            prob2 = [")" + prev for prev in prob2]
        return prob1 + prob2
