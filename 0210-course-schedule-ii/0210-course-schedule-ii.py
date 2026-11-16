from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph={}
        indegree = [0]*numCourses
        q=deque([])
        for i in range(numCourses):
            graph[i]=[]
        for i in prerequisites:
            x=i[0]
            y=i[1]
            graph[y].append(x)
        for i in range(numCourses):
            for j in graph[i]:
                indegree[j]+=1
        res=[]
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            x=q.popleft()
            res.append(x)
            for i in graph[x]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        if len(res)==numCourses:
            return res
        return []

        

        