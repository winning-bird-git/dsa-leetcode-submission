class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        grph={}
        for i in range(numCourses):
            grph[i]=[]
        for i in prerequisites:
            ai = i[1]
            bi = i[0]
            grph[ai].append(bi)
        
        def dfs(st,grph,visited,node,dfsvisit):
            visited[node]=1
            dfsvisit[node]=1
            for i in grph[node]:
                if visited[i]!=1:
                    if not dfs(st,grph,visited,i,dfsvisit):
                        return False 
                elif dfsvisit[i]==1:
                    return False 
            dfsvisit[node]=0
            return True


        st=[]
        visited = [-1]*numCourses
        dfsvisit = [-1]* numCourses
        for i in grph:
            if visited[i]!=1:
                if not dfs(st,grph,visited,i,dfsvisit):
                    return False 
        return True
    


         
        