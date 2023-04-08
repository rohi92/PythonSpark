class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dict={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                increasing_series=[]
                visited=[[i,j]]
                increasing_series.append(matrix[i][j])
                self.dfs(matrix,i,j,increasing_series,visited)
                dict[(i,j)]=increasing_series
        return dict

    def dfs(self,matrix,i,j,increasing_series,visited):

        dfs_vertex=[]
        adjacent_nodes=[[0,1],[1,0],[-1,0],[0,-1]]
        for k in adjacent_nodes:
            new_row=k[0]+i
            new_col=k[1]+j

            if new_row>=0 and new_row <len(matrix) and new_col>=0 and new_col <len(matrix[0]) and [new_row,new_col] \
                    not in visited:
                visited.append([new_row, new_col])

                if matrix[i][j]<matrix[new_row][new_col]:

                    increasing_series.append(matrix[new_row][new_col])
                    visited=[new_row,new_col]
                    self.dfs(matrix,new_row,new_col,increasing_series,visited)
        dfs_vertex.append([increasing_series])


        return



if __name__=="__main__":
    sol=Solution()
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    print(sol.longestIncreasingPath(matrix))

