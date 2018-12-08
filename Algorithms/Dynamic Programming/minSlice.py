class Solution:
    def MinSliceWeight(self, Matrix):
        N = len(Matrix[0])
        C = [[0 for i in range(N)] for i in range(N)]
        for col in range(N):
            C[0][col] = Matrix[0][col]
        print(C)
            # //Run dynamic program
        for row in range(1, N) :
            for col in range(N):
                if row-1 >= 0 and col-1>=0 and col+1<N:
                    C[row][col] = Matrix[row][col] + min(C[row - 1][col - 1], C[row - 1][col], C[row - 1][col + 1])
        # print(C)

test = Solution()
test.MinSliceWeight([[1,2,3],[4,5,6],[7,8,9]])