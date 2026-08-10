from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        ans = [[0]*m for _ in range(n)]
        q=deque([])
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    ans[i][j]=9999999
                else:
                    q.append([i,j,0])
        while q:
            obj=q.popleft()
            r=obj[0]
            c=obj[1]
            dis=obj[2]
            rcheck=[-1,0,1,0]
            ccheck=[0,1,0,-1]

            for i in range(len(rcheck)):
                exr= r+rcheck[i]
                exc= c+ccheck[i]
                if exr>=0 and exr<n and exc>=0 and exc<m and ans[exr][exc]!=0 :
                    if dis+1<ans[exr][exc]:
                        ans[exr][exc] = dis+1
                        q.append([exr,exc,ans[exr][exc]])

        return ans


    



        