# https://leetcode.cn/problems/word-search-ii/?envType=study-plan-v2&envId=top-interview-150

def test():
     board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
     words = ["oath","pea","eat","rain"]
     ans = word_search(board, words)
     assert ans.sort() == ["eat","oath"].sort()


def test2():
     board = [["A" ] ]
     word = "A"
     ans = word_search(board, word)
     assert ans == True

from collections import defaultdict
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""
        self.is_word = False

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word

def word_search(board, words):
    if not board or not board[0]:
        return False
    ans = []
    n = len(board)
    m = len(board[0])
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]

    trie = Trie()
    for word in words:
        trie.insert(word)

    def is_inboard(i,j):
        return 0<=i<n and 0<=j<m

    def backtrace(t:Trie, i, j):

        for letter in t.children:
            if letter != board[i][j]:
                continue
            child = t.children[letter]
            if child.is_word:
                ans.append(child.word)

            board[i][j] = "#"
            for dx, dy in dirs:
                x = i+dx
                y = j+dy
                if not is_inboard(x, y):
                    continue
                backtrace(child, x, y)
            board[i][j] = letter
        return


    for i in range(n):
        for j in range(m):
            backtrace(trie, i, j)
    return ans

