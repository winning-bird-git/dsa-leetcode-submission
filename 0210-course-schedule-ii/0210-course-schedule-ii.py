from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph={}
        indegree=[0]*numCourses
        q=deque([])
        for i in prerequisites:
            u=i[0]
            v=i[1]
            if v not in graph:
                graph[v]=[u]
            else:
                graph[v].append(u)
        for i in graph:
            for j in graph[i]:
                indegree[j]+=1
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        res=[]
        while q:
            x=q.popleft()
            res.append(x)
            if x in graph:
                for i in graph[x]:
                    indegree[i]-=1
                    if indegree[i]==0:
                        q.append(i)
        if len(res)==numCourses:
            return res
        else:
            return []


        

        