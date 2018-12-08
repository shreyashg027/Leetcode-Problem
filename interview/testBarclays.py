def lcs(str1, str2, x, y):
    lis = [[0 for x in range(y + 1)] for x in range(x + 1)]
    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                lis[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                lis[i][j] = lis[i-1][j-1] + 1
            else:
                lis[i][j] = max(lis[i-1][j], lis[i][j-1])

    pointer = lis[x][y]
    common_seq = [""] * (pointer+1)
    common_seq[pointer] = ""
    i = x
    j = y
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            common_seq[pointer-1] = str1[i - 1]
            j -= 1
            pointer -= 1
            i -= 1
        elif lis[i-1][j] > lis[i][j-1]:
            i -= 1
        else:
            j -= 1
    return "".join(common_seq)
a = 'XMJYAUZ'
b = 'MZJAWXU'
x = len(a)
y = len(b)
print(lcs(a, b, x, y))
