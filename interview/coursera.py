def max_length(a, k):
    sum = 0
    count = 0
    maxCount = 0
    for i in range(len(a)):
        if (sum + a[i]) <= k:
            sum += a[i]
            count += 1

        elif sum != 0:
            sum = sum - a[i - count] + a[i]
        maxCount = max(count, maxCount)
    return maxCount





ans = max_length([3, 1, 2, 1], 4)
print(ans)