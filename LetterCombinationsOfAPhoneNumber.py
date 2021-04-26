class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.dic = {"2": ["a","b","c"],
              "3": ["d","e","f"],
              "4": ["g","h","i"],
              "5": ["j","k","l"],
              "6": ["m","n","o"],
              "7": ["p","q","r","s"],
              "8": ["t","u","v"],
              "9": ["w","x","y","z"]}
        
        if digits == "":
            return []
        
        return self.rec(digits,0)
    
    def rec(self,digits,idx):
        letters = self.dic[digits[idx]]
        if len(digits) == idx+1:
            return letters
        comb = self.rec(digits,idx+1)
        newComb = []
        for l in letters:
            newComb += [l + c for c in comb]
        return newComb
