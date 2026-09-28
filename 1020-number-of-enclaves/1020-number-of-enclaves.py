from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited= [[0]*n for _ in range(m)]
        q=deque([])

        for i in range(n):
            if grid[0][i]==1:
                q.append([0,i])
            if grid[m-1][i]==1:
                q.append([m-1,i])
        for i in range(m):
            if grid[i][0]==1:
                q.append([i,0])
            if grid[i][n-1]==1:
                q.append([i,n-1])
        while q:
            x=q.popleft()
            a=x[0]
            b=x[1]
            visited[a][b]=1
            x1=[-1,0,1,0]
            y1=[0,1,0,-1]
            for i in range(len(x1)):
                nx=a+x1[i]
                ny=b+y1[i]
                if nx>=0 and nx<m and ny>=0 and ny<n and grid[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append([nx,ny])
        c=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j]==0:
                    c+=1

        return c

        