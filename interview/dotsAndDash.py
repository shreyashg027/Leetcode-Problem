class Solution:
    def dotsansdash(self,matString,m,n):
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                val = 0
                if mat[i][j] == '.':
                    if i-1>=0:
                        if mat[i-1][j] == '*':
                            val += 1
                    if j-1>=0:
                        if mat[i][j-1] == '*':
                            val += 1
                    if i-1>=0 and j-1>=0:
                        if mat[i-1][j-1] == '*':
                            val += 1
                    if i+1<len(mat):
                        if mat[i+1][j] == '*':
                            val += 1
                    if j+1<len(mat[0]):
                        if mat[i][j+1] == '*':
                            val += 1
                    if i+1<len(mat) and j+1<len(mat[0]):
                        if mat[i+1][j+1] == '*':
                            val += 1
                    if i-1>=0 and j+1<len(mat[0]):
                        if mat[i-1][j+1] == '*':
                            val += 1
                    if i+1<len(mat) and j-1>=0:
                        if mat[i+1][j-1] == '*':
                            val += 1
                    # mat[i][j] = str(val)


test = Solution()
string1 = '3,5;**.........*...'
line = string1.split(';')
num = line[0].split(',')
m,n = int(num[0]),int(num[1])
matString = line[1]


mat = ['*','*','.','.','.','.','.','.','.','.','.','*','.','.','.']
# print(test.dotsansdash(mat,3,5))
# print(''.join(mat))

l = ['.','2','2','2','2','2']
str1 = ''
# str1 += [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
# print(mat)

