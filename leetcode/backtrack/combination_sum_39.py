def test():
    candidates = [2,3,6,7]
    target = 7
    ans = combinatinon_sum(candidates, target)
    # [[2, 2, 3], [7]]

    print(ans)
    ans = combinatinon_sum2(candidates, target)
    # [[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]
    print(ans)

def combinatinon_sum2(candidates, target):
    path = []
    ans = []
    def backtrace(candidates, target):
        if target == 0:
            ans.append(path[:])
        for num in candidates:
            if num > target:
                return
            path.append(num)
            backtrace(candidates, target-num)
            path.pop()
    backtrace(candidates, target)
    return ans

def combinatinon_sum(candidates, target):
    path = []
    ans = []
    def backtrace(candidates, start, target):
        if target == 0:
            ans.append(path[:])
        for index in range(start, len(candidates)):
            num = candidates[index]
            if num > target:
                return

            path.append(num)
            backtrace(candidates, index, target-num)
            path.pop()
    backtrace(candidates, 0, target)
    return ans
