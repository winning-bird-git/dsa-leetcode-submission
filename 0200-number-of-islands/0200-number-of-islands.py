from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visit=[[0]*m for _ in range(n)]
        q=deque([])
        def bfs(q,visit,grid):
            while q:
                obj=q.popleft()
                r=obj[0]
                c=obj[1]
                delr=[-1,0,1,0]
                delc=[0,1,0,-1]
                for i in range(len(delr)):
                    er=r+delr[i]
                    ec=c+delc[i]
                    if er>=0 and er<n and ec>=0 and ec<m and visit[er][ec]==0 and grid[er][ec]=="1":
                        visit[er][ec]=1
                        q.append([er,ec])

        c=0
        for i in range(n):
            for j in range(m):
                if visit[i][j]==0 and grid[i][j]=="1":
                    c+=1
                    q.append([i,j])
                    visit[i][j]=1
                    bfs(q,visit,grid)
        return c
        

        