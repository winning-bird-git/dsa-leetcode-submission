from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        q=deque([])
        visited=[[0]*n for _ in range(m)]
        for i in range(m):
            if board[i][0]=="O":
                visited[i][0]=1
                q.append([i,0])
            if board[i][n-1]=="O":
                visited[i][n-1]=1
                q.append([i,n-1])
        for i in range(n):
            if board[0][i]=="O":
                visited[0][i]=1
                q.append([0,i])
            if board[m-1][i]=="O":
                visited[m-1][i]=1
                q.append([m-1,i])
        while q:
            obj=q.popleft()
            r=obj[0]
            c=obj[1]
            xr=[-1,0,1,0]
            xc=[0,1,0,-1]
            for i in range(len(xr)):
                nr=r+xr[i]
                nc=c+xc[i]
                if nr>=0 and nr<m and nc>=0 and nc<n and board[nr][nc]=="O" and visited[nr][nc]!=1:
                    visited[nr][nc]=1
                    q.append([nr,nc])
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and visited[i][j]!=1:
                    board[i][j]="X"
        