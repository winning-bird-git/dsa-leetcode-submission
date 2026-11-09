
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n= len(isConnected)
        visited =[-1]*len(isConnected)
        def dfs(isConnected,visited,node):
            visited[node]=1
            for i in range(n):
                for j in range(n):
                    if isConnected[node][j]==1 and visited[j]!=1:
                        dfs(isConnected,visited,j)

        c=0
        for i in range(n):
            if visited[i]== -1:
                c+=1
                dfs(isConnected,visited,i)
        return c


        
