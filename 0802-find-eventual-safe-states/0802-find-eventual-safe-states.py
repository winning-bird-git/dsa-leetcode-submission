from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # reverse edges to use topo sort
        g={}
        indegree = [0]*len(graph)
        for i in range(len(graph)):
            for j in graph[i]:
                if j not in g:
                    g[j]=[i]
                    indegree[i]+=1
                else:
                    g[j].append(i)
                    indegree[i]+=1
        q=deque([])
        res=[]
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
                res.append(i)
        while q:
            x=q.popleft()
            if x in g:
                for i in g[x]:
                    indegree[i]-=1
                    if indegree[i]==0:
                        q.append(i)
                        res.append(i)
        res.sort()
        return res
        



                    


        