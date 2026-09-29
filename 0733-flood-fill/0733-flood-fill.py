from collections import deque 
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image 
        n=len(image)
        m=len(image[0])
        oc=image[sr][sc]
        image[sr][sc]=color
        q=deque([[sr,sc]])
        while q:
            obj=q.popleft()
            r=obj[0]
            c=obj[1]
            x=[-1,0,1,0]
            y=[0,1,0,-1]
            for i in range(len(x)):
                nr=r+x[i]
                nc=c+y[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and image[nr][nc]==oc:
                    image[nr][nc]=color
                    q.append([nr,nc])
        return image 
