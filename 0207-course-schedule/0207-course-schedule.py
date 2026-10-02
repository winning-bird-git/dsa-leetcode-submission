class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph={}
        for i in prerequisites:
            u=i[0]
            v=i[1]
            if u not in graph:
                graph[u]=[v]
            else:
                graph[u].append(v)
        print(graph)
        n=numCourses
        visited=[0]*n
        dfsvisit=[0]*n
        def dfs(node,visited,dfsvisit,graph):
            visited[node]=1
            dfsvisit[node]=1
            if node in graph:
                for i in graph[node]:
                    if visited[i]!=1:
                        if not dfs(i,visited,dfsvisit,graph):
                            return False
                    elif dfsvisit[i]==1:
                        return False
            dfsvisit[node]=0
            return True

        for i in range(n):
            if visited[i]!=1:
                if not dfs(i,visited,dfsvisit,graph):
                    return False
        return True 
        