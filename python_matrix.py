from typing import List
# 542. 01 Matrix

class Solution:
    # using BFS and queue
    def updateMatrix(self, mx: List[List[int]]) -> List[List[int]]:
      r,c=len(mx),len(mx[0])
      def bfs(mx,a,b):
        st=[[a,b,0]]
        while st:
          m,n,s=st.pop(0)
          
          if mx[m][n]==0: 
            mx[a][b]=s 
            return 0
            
          for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
            j=m+x
            k=n+y
            if 0<=j<r and 0<=k<c: st.append([j,k,s+1])
      
      for i in range(r):
        for j in range(c):
          if mx[i][j]==1:
            bfs(mx,i,j)
      return mx

may = [[0,0,0],[0,1,1],[1,1,1]]

solution = Solution()
print(solution.updateMatrix(may))



