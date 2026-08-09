class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        def depthfun(depth,parent,curr):
            if depth[curr]!=0:
                return 
            if parent[curr]==-1:
                depth[curr]=1
                return 
            depthfun(depth,parent,parent[curr])
            depth[curr]=depth[parent[curr]]+1


        depth=[0]*len(parent)
        for i in range(len(depth)):
            depthfun(depth,parent,i)
        

        h = max(depth)
        ans=0
        for i in range(len(nums)):
            x=nums[i]*(h-depth[i]+1)
            ans+=x
        return ans 
            
            
        