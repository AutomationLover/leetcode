def test():
     board = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
     word = "ABCCED"
     ans = word_search(board, word)
     assert ans == True
def test2():
     board = [["A" ] ]
     word = "A"
     ans = word_search(board, word)
     assert ans == True
def word_search(board, word):
    if not board or not board[0]:
        return False
    n = len(board)
    m = len(board[0])
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    def is_inboard(i,j):
        return 0<=i<n and 0<=j<m

    def backtrace(word, i, j):
        if word[0] != board[i][j]:
            return False
        if len(word) == 1:
            return True
        board[i][j] = "#"
        for dx, dy in dirs:
            x = i+dx
            y = j+dy
            if not is_inboard(x, y):
                continue
            if backtrace(word[1:], x, y):
                return True
        board[i][j] = word[0]
        return False

    for i in range(n):
        for j in range(m):
            if backtrace(word, i, j):
                return True
    return False

