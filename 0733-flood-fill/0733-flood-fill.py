from collections import deque 
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
        
        tocolor=image[sr][sc]
        image[sr][sc]=color
        q=deque([[sr,sc]])
        #adding this condition to avoid infinite loop
        #inpython visit=image doesnt create new arraymaps to same obj
        if tocolor==color:
            return image
        while q:
            obj=q.popleft()
            row=obj[0]
            col=obj[1]
            rowcheck=[-1,0,1,0]
            colcheck=[0,1,0,-1]
            for i in range(len(rowcheck)):
                exrow=row+rowcheck[i]
                excol=col+colcheck[i]
                if exrow>=0 and exrow<n and excol>=0 and excol<m and image[exrow][excol]== tocolor:
                    image[exrow][excol]=color
                    q.append([exrow,excol])
        return image 




    

        