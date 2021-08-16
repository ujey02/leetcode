#92.66 / 34.79
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if s == "":
            return [""]
        
        #remove all ")"s in front and "(" in back
        while s != "" and s[0] is ")":
            s = s[1:]
        while s != "" and s[-1] is "(":
            s = s[:-1]
            
        #find and count wrongly placed close/open brackets
        exceed_close = []
        exceed_open = []
        fw_count = 0
        bw_count = 0
        for i in range(len(s)):
            fw = s[i]
            bw = s[-1 * i - 1]
            
            if fw == "(":
                fw_count += 1
            elif fw == ")":
                fw_count -= 1
            
            if bw == "(":
                bw_count += 1
            elif bw == ")":
                bw_count -= 1
            
            if fw_count < 0:
                exceed_close.append(i)
                fw_count = 0
            if bw_count > 0:
                exceed_open.append(-1 * i - 1)
                bw_count = 0
        
        print(exceed_close, exceed_open)
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
            # print(self.closeRemoved)
            # print(s[exceed_open[-1]:], self.openRemoved)
            for front in self.closeRemoved:
                for back in self.openRemoved:
                    ans.append(front+back)
            return ans
                
        
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
                
                
