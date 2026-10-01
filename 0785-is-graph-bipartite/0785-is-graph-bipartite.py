from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        visited=[-1]*n
        def dfs(graph,visited,node,color):
            visited[node]=color
            for i in graph[node]:
                if visited[i]==-1:
                        if not dfs(graph,visited,i,1-color):
                            return False
                elif color==visited[i]:
                    return False
            return True


        for i in range(n):
            if visited[i]==-1:
                if dfs(graph,visited,i,0)==False:
                    return False
        return True

        
        