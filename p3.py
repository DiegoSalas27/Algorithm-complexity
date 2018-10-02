def s(a, n, m):
    for i in range(len(a)):
        if s(a[:i]+a[i+1:],n,m+a[i]) or s(a[:i]+a[i+1:],n,m-a[i]) or s(a[:i]+a[i+1:],n,m*a[i]): return True
    return n == m

def solv2(nums, n):
    if len(nums) == 1:
        return nums[0] == n

    for i in range(len(nums)):
        a = nums[i]
        nums1 = nums[:i] + nums[i+1:]
        
        n1 = n + a
        n2 = n - a
        n3 = n // a
        if solv2(nums1, n1) or solv2(nums1, n2) or (n%a==0 and solv2(nums1, n3)):
            return True
        
    return False


print(s([3, 2, 1, 4, 5], 23, 0))
print(s([1, 2, 3, 4, 5], 23, 0))
print(s([2, 3, 5, 7, 11], 23, 0))
print(s([1, 1, 1, 1, 1], 23, 0))
