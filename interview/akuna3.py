def flip_signs(s,K):
    op = 0
    minusStr = '-'*K
    plusStr = '+'*K
    op += s.count(minusStr)
    # print(op)
    s = s.replace(minusStr, plusStr)
    s = list(s)
    for i in range(len(s)):
        if s[i] == '-':
            # print(s)
            if i+K <= len(s):
                op += 1
                s[i] = '+'
                for j in range(1,K):
                    if s[i+j] == '-':

                        s[i+j] = '+'
                    else:
                        s[i+j] = '-'
    if '-' in s:
        return -1
    else:
        return op


ans = flip_signs('-----', 5)
print(ans)
