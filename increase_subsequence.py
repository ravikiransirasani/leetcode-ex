def longest_increasing_subseq(lst):
    n = len(lst)
    arr = [1]*n
    for i in range(1,n):
        for j in range(i):
            if lst[i]> lst[j]:
                arr[i] = max(arr[i],arr[j]+1)
    return max(arr)
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
nums1 = [10, 20, 30, 40, 50, 60, 70, 80]

print(f'longest_increasing_subseq--{longest_increasing_subseq(nums)}')
print(f'longest_increasing_subseq--{longest_increasing_subseq(nums1)}')

from collections import defaultdict
def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] +=1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                total += dp[j][diff]
    return total

nums = [2,4,6,8,10]
print(f'numberOfArithmeticSlices--{numberOfArithmeticSlices(nums)}')
