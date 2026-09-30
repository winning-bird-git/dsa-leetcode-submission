from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([i,j,0])
        ans = 0
        while q:
            obj=q.popleft()
            r=obj[0]
            c=obj[1]
            t=obj[2]
            ans=max(ans,t)
            xr=[-1,0,1,0]
            xc=[0,1,0,-1]
            for i in range(len(xr)):
                nr=r+xr[i]
                nc=c+xc[i]
                if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    q.append([nr,nc,t+1])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return ans 


        