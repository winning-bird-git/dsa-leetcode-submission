from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
       visited = [0]*len(isConnected)
       def dfs(node,graph,visited):
        visited[node]=1
        for i in range(len(graph)):
            if graph[node][i]==1 and visited[i]!=1:
                dfs(i,graph,visited)

       c=0
       for i in range(len(isConnected)):
        if visited[i]!=1:
            c=c+1
            dfs(i,isConnected,visited)
       return c 