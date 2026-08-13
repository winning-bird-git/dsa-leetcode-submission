from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visit = [-1]* len(graph)
        q=deque([])
        
        for i in range(len(visit)):
            if visit[i]!= -1:
                continue
            q.append([i,0])
            visit[i]=0
            while q:
                print(q)
                obj=q.popleft()
                precol=obj[1]
                for i in graph[obj[0]]:
                    if visit[i]==-1:
                        if precol==0:
                            q.append([i,1])
                            visit[i]=1
                        elif precol==1:
                            q.append([i,0])
                            visit[i]=0
                    else:
                        if precol==visit[i]:
                            return False
               
            
        return True

        