from collections import deque 
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
        visit=image
        tocolor=image[sr][sc]
        visit[sr][sc]=color
        q=deque([[sr,sc]])
        while q:
            obj=q.popleft()
            row=obj[0]
            col=obj[1]
            rowcheck=[-1,0,1,0]
            colcheck=[0,1,0,-1]
            for i in range(len(rowcheck)):
                exrow=row+rowcheck[i]
                excol=col+colcheck[i]
                if exrow>=0 and exrow<n and excol>=0 and excol<m and image[exrow][excol]== tocolor and visit[exrow][excol]!=color:
                    q.append([exrow,excol])
                    visit[exrow][excol]=color
        return visit 




    

        