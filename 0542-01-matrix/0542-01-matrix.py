from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        visited=[[0]*n for _ in range(m)]
        q=deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append([i,j,0])
                    visited[i][j]=1
        while q:
            obj=q.popleft()
            r=obj[0]
            c=obj[1]
            ans=obj[2]
            xr=[-1,0,1,0]
            xc=[0,1,0,-1]
            for i in range(len(xr)):
                nr=r+xr[i]
                nc=c+xc[i]
                if nr>=0 and nr<m and nc>=0 and nc<n and visited[nr][nc]==0 and mat[nr][nc]==1:
                    mat[nr][nc]=ans+1
                    visited[nr][nc]=1
                    q.append([nr,nc,ans+1])
        return mat 

        