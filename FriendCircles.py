class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        if n == 1:
            return 1        
        eids = {}
        
        for i in range(n):      
            if i not in eids: #if not connected to any yet
                eids[i] = -1
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    if eids[i] == -1: 
                        eids[i] = i
                    if j in eids and eids[i] > eids[j]:
                        if eids[eids[i]] > eids[j]:
                            eids[eids[i]] = eids[j]
                        eids[i] = eids[j]
            if eids[i] == -1:
                continue
                            
            for j in range(i+1, n):
                #directly connected
                if isConnected[i][j] == 1:
                    # print(i, " is connected to ", j)
                    if j in eids:
                        prev_eid = eids[j]
                        eids[prev_eid] = min(eids[prev_eid],eids[i])
                    eids[j] = eids[i]
                        
            # print('i:{},eid:{},eids:{}'.format(i, eid,eids))  
        
        count = 0
        for i in range(n):
            if eids[i] == -1:
                count += 1
                del eids[i]
            elif eids[i] > eids[eids[i]]:
                eids[i] = eids[eids[i]]
                
        # print(eids)
        # print(set(eids.values()))
        # print(eid, len(set(eids.values())), count)
        return len(set(eids.values())) + count
