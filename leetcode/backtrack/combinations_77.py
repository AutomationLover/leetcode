def combination1(n, k):
    path = []
    ans = []
    def backtrack(k):
        if k == 0:
            ans.append(path[:])
            return
        for i in range(1, n+1):
            if i in path:
                continue
            path.append(i)
            backtrack(k-1)
            path.pop()
    backtrack(k)
    return ans

def combination2(n, k):
    path = []
    ans = []
    def backtrack(n, k):
        if k == n:
            ans.append(path+[n-i for i in range(n)])
            return
        if k == 0:
            ans.append(path[:])
            return
        backtrack(n-1, k)

        path.append(n)
        backtrack(n-1, k-1)
        path.pop()

    backtrack(n, k)
    return ans

def test():
    n = 4
    k = 2

    print()
    ans = combination1(n, k)
    print(ans)

    ans = combination2(n, k)
    print(ans)

def permutations(nums):
    path = []
    ans = []
    def backtrace(nums):
        if len(path) == len(nums):
            ans.append(path[:])
        for i in nums:
            if i in path:
                continue
            path.append(i)
            backtrace(nums)
            path.pop()
    backtrace(nums)
    return ans
#https://leetcode.cn/problems/permutations/description/?envType=study-plan-v2&envId=top-interview-150
def test_permutations():
    nums = [1,2,3]
    ans = permutations(nums)
    print(ans)

