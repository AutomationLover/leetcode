# https://leetcode.cn/problems/trapping-rain-water-ii/description/
# 407. 接雨水 II 解法 options:
# - Dijkstra 解法
# - 排序 + 并查集
def boundary(row: int, column: int, offsets=None):
    if offsets is None:
        offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def around(r: int, c: int, valid=None):
        for dr, dc in offsets:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < column:
                if valid is None or valid(nr, nc):
                    yield nr, nc

    return around

class Solution:
    def trapRainWater(self, heights) -> int:
        m, n = len(heights), len(heights[0])
        arr = [(heights[i][j], i, j) for j in range(n) for i in range(m)]
        arr.sort(key=lambda it:it[0])

        f = list(range(m * n + 1))
        cnt = [0] * (m * n + 1)
        cnt[0] = 0
        hs = [0] * (m * n + 1)
        ans = 0

        def find(i):
            if i != f[i]:
                f[i] = find(f[i])
            return f[i]

        def union(i, j, h):
            nonlocal ans
            fi, fj = find(i), find(j)
            if fi != fj:
                if fi > fj:
                    fi, fj = fj, fi
                f[fj] = fi
                cnt[fi] += cnt[fj]
                if cnt[fi]> 1:
                    print(cnt[fi])
                hs[fi] += hs[fj]
                if fi == 0:  # boarder 边界
                    ans += h * cnt[fj] - hs[fj]



        around = boundary(m, n)
        for h, i, j in arr:
            ij = i * n + j + 1
            cnt[ij], hs[ij] = 1, h
            for ni, nj in around(i, j):
                nij = ni * n + nj + 1
                if cnt[nij] > 0:  # 如果nij没有访问过，不处理，等下次访问到nij再处理
                    union(ij, nij, h)
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:  # 边界，到达边界可以计算盛水
                union(0, ij, h)

        return ans

def test_bincha():
    heightMap = [[1,4,3,1,3,2],
                 [3,2,1,3,2,4],
                 [2,3,3,2,3,1]]
    a = Solution().trapRainWater(heightMap)
    print(a)


def trapRainWater(heights):
    m, n = len(heights), len(heights[0])
    arr = [(heights[i][j], i, j) for j in range(n) for i in range(m)]


def test_dfs():
    heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    a = trapRainWater(heightMap)
    print(a)


# 大致思路就是以边界为起点，从最低开始往内推，保留最高的边界高度（或本身是个边界）。
# 因为优先队列保证了每次第一次访问到一个点，一定是该点能存的雨水的最高高度了（它是后面所有高度最矮的）。

import heapq
class Solution2:
    def trapRainWater(self, heightMap) -> int:
        m, n, ans = len(heightMap), len(heightMap[0]), 0
        visited = [[False] * n for _ in range(m)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        pq =   []
        # 边界放入pq
        for i in range(1,n-1):
            heapq.heappush(pq,(heightMap[0][i], 0, i))
            heapq.heappush(pq,(heightMap[m-1][i], m-1, i))
        for i in range(1,m-1):
            heapq.heappush(pq, (heightMap[i][0], i, 0))
            heapq.heappush(pq, (heightMap[i][n-1], i, n-1))
        while pq:
            h, x, y = heapq.heappop(pq)
            for dx, dy in dirs:
                nx, ny = x+dx,y+dy
                if 0 < nx < m - 1 and 0 < ny < n - 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    ans += max(0, h - heightMap[nx][ny])
                    heapq.heappush(pq, (max(h, heightMap[nx][ny]), nx, ny))
        return ans

