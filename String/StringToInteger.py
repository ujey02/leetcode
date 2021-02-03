class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        ans = ""
        isReadStart = False
        tf = True
        sign = 1
        
        for i in range(len(s)):
            ch = s[i]
            
            if isReadStart: #reading digit started
                if not (ord(ch) > 47 and ord(ch) < 58):
                    break
                else:
                    ans += ch
                    
            elif not isReadStart: #hasn't read any digits yet
                if ch == ' ': continue
                elif (ch == '-' or ch == "+"):
                    sign = int(ch+'1')
                    isReadStart = True
                elif (ord(ch) > 47 and ord(ch) < 58):
                    isReadStart = True
                    ans += ch
                else:
                    break
                    

# #             if ord(ch) > 48 and ord(ch) < 58: #ch is 1~9
# #                     ans += ch
# #                     isReadStart = True
# #             elif ord(ch) == 48: #ch is 0
# #                 isReadStart = True
# #                 if ans == "": continue
# #                 else: ans += ch
                    
# #             elif ch == ' ' and not isReadStart:
# #                 continue
# #             elif (ch == '-' or ch == "+") and not isReadStart:
# #                 sign = int(ch+'1')
# #                 isReadStart = True
# #             else:
# #                 break
            
        if ans == '':
            return 0
        elif int(ans)*int(sign) > 2**31 - 1:
            return 2**31-1
        elif int(ans)*int(sign) < -1*2**31:
            return -1*2**31
        else:
            return int(ans)*sign
            
