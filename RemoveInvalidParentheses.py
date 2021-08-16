#97.49 / 34.79
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if s == "":
            return [""]
        
        #remove all ")"s in front and "(" in back
        while s != "" and s[0] is ")":
            s = s[1:]
        while s != "" and s[-1] is "(":
            s = s[:-1]
            
        exceed_close = self.findInvalid(s, 1)
        exceed_open = self.findInvalid(s, -1)
        
        self.check = {}
        self.closeRemoved, self.openRemoved = [], []
        if not exceed_close and not exceed_open: # all are placed right
            return [s]
        elif exceed_close and not exceed_open: # wrong close bracket(s) exist
            self.middle = s[exceed_close[-1]+1:]
            self.removeClose("", s[:exceed_close[-1]+1] , len(exceed_close), 0)
            return self.closeRemoved
        
        elif not exceed_close and exceed_open: #wrong open bracket(s) exist
            self.middle = s[:exceed_open[-1]]
            self.removeOpen("", s[exceed_open[-1]:], len(exceed_open), 0)
            return [self.middle + back for back in self.openRemoved]
        
        else:  # wrong close and open brackets exist
            self.middle = s[exceed_close[-1]+1:exceed_open[-1]]
            self.removeClose("", s[:exceed_close[-1]+1] , len(exceed_close), 0)
            self.check = {}
            self.removeOpen("", s[exceed_open[-1]:], len(exceed_open), 0)
            ans = []
            for front in self.closeRemoved:
                for back in self.openRemoved:
                    ans.append(front+back)
            return ans
    
    def findInvalid(self, s, flag = 1):
        exceed = []
        count = 0
        n = len(s)
        for i in range(flag * min(flag*n, 0) + min(flag, 0), max(flag*n, 0) + min(flag, 0), flag):
            c = s[i]
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
            
            if flag * count < 0:
                exceed.append(i)
                count = 0
        return exceed
        
    def removeClose(self, prev_s, s, n, count):
        '''
        prev_s: previous string
        s: current string to analyze
        n: number of brackets left to be removed
        count: count of brackets
        '''
        if n == 0:
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
            if (prev_s + s + self.middle, -1) not in self.check and count == 0:
                self.closeRemoved.append(prev_s + s + self.middle)
                self.check[(prev_s + s + self.middle, -1)] = 1
        elif len(s) < n:
            return
        else:
            for i, c in enumerate(s):
                if c == ")":
                    if (prev_s+s[:i], n-1) not in self.check:
                        self.check[(prev_s+s[:i], n-1)] = 1
                        self.removeClose(prev_s+s[:i],s[i+1:], n-1, count)
                    if (prev_s+s[:i+1], n) not in self.check and count > 0:
                        count -= 1
                        self.check[(prev_s+s[:i+1], n)] = 1
                        self.removeClose(prev_s+s[:i+1], s[i+1:], n, count)
                elif c == "(":
                    count += 1

    def removeOpen(self, prev_s, s, n, count):
        '''
        prev_s: previous string
        s: current string to analyze
        n: number of brackets left to be removed
        count: count of brackets
        '''
        if n == 0:
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
            if (s + prev_s, -1) not in self.check and count == 0:
                self.openRemoved.append(s + prev_s)
                self.check[(s + prev_s, -1)] = 1 
        elif len(s) < n:
            return
        else:
            for i in range(len(s)-1,-1,-1):
                c = s[i]
                if c == "(":
                    if (s[i+1:]+prev_s, n-1) not in self.check:
                        self.check[(s[i+1:]+prev_s, n-1)] = 1
                        self.removeOpen(s[i+1:]+prev_s, s[:i], n-1, count)
                    if (s[i:]+prev_s, n) not in self.check and count < 0:
                        count += 1
                        self.check[(s[i:]+prev_s, n)] = 1
                        self.removeOpen(s[i:]+prev_s, s[:i], n, count)
                elif c == ")":
                    count -= 1
