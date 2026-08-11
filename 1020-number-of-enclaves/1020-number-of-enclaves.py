from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n= len(grid)
        m= len(grid[0])
        q=deque([])
        visit=[[0]*m for _ in range(n)]
        for i in range(m):
            if grid[0][i]==1:
                visit[0][i]=1
                q.append([0,i])
            if grid[n-1][i]==1:
                visit[n-1][i]=1
                q.append([n-1,i])
        for i in range(n):
            if grid[i][0]==1:
                visit[i][0]=1
                q.append([i,0])
            if grid[i][m-1]==1:
                visit[i][m-1]=1
                q.append([i,m-1])
        while q:
            obj=q.popleft()
            r=obj[0]
            c=obj[1]
            dr=[-1,0,1,0]
            dc=[0,1,0,-1]
            for i in range(len(dr)):
                er=r+dr[i]
                ec=c+dc[i]
                if er>=0 and er<n and ec>=0 and ec<m and grid[er][ec]==1 and visit[er][ec]!=1:
                    visit[er][ec]=1
                    q.append([er,ec])
       

        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and visit[i][j]!=1:
                    ans=ans+1
        return ans 





        