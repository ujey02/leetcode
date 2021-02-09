class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle): return -1
        elif len(haystack) == 0 and len(needle) == 0:
            return 0
        elif len(haystack) == 0: return -1
        elif len(needle) == 0: return 0
        
        ans = -1
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                ans = self.checkNeedle(haystack[i:], needle, i)
                if ans != -1:
                    return ans
        return ans
        
    def checkNeedle(self, haystack, needle, idx):
        counter = 0
        lenNeedle = len(needle)
        ans = -1
        
        for i in range(len(haystack)):
            h_i = haystack[i]
            n_i = needle[counter]
            
            if h_i == n_i:
                if counter == 0:
                    ans = i+idx
                counter += 1
                if counter == lenNeedle:
                    return ans
            else:
                return -1
                
        return ans
            
