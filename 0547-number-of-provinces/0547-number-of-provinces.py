from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = [-1]* len(isConnected)
        ans =0

        for i in range(len(isConnected)):
            if visit[i]== -1:
                visit[i]=1
                ans+=1
                q=deque([i])
                while q:
                    ver = q.popleft()
                    for j in range(len(isConnected)):
                        if isConnected[ver][j] ==1 and visit[j]==-1:
                            visit[j]=1
                            q.append(j)
        return ans 

       