from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited = [[0]*n for _ in range(m)]
        c=0
        def bfs(r,c,visited,grid):
            visited[r][c]=1
            q=deque([[r,c]])
            while q:
                obj=q.popleft()
                r1=obj[0]
                c1=obj[1]
                xr=[-1,0,1,0]
                xc=[0,1,0,-1]
                for i in range(len(xr)):
                    nr=r1+xr[i]
                    nc=c1+xc[i]
                    if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]=="1" and visited[nr][nc]==0:
                        visited[nr][nc]=1
                        q.append([nr,nc])

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and visited[i][j]!=1:
                    c+=1
                    bfs(i,j,visited,grid)
        return c 