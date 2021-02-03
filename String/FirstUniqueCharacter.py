class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for i in range(len(s)):
        #     if len(s.split(s[i])) == 2:
        #         return i
        # return -1
        
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [1,i]
            else:
                dic[s[i]][0] += 1
                
        for key in dic.keys():
            if dic[key][0] == 1:
                return dic[key][1]
        return -1
