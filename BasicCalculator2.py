class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        exp = [[],[]]
        
        count = 0
        length = len(s)
        a = ""
        
        while count < length:
            c = s[count]
            # print(c,a)
            if ord(c) > 47:
                a += c
                count += 1
            elif c == "*" or c == "/":
                count += 1
                b = ""
                while count < length and ord(s[count]) > 47:
                    b += s[count]
                    count += 1
                if c == "*":
                    a = int(a) * int(b)
                else:
                    a = int(a) // int(b)
            else:
                exp[0].append(c)
                exp[1].append(int(a))
                a = ""    
                count += 1
            
        exp[1].append(int(a))
        
        ans = exp[1][0]

        for i in range(len(exp[0])):
            if exp[0][i] == "+":
                ans += exp[1][i+1]
            else:
                ans -= exp[1][i+1]
        return ans
            
            
        
                
                
        #now we have array of integers and operators in exp 
        #ex) s = "3+2*2", exp = [[+],[3,4]]
        
            
            
