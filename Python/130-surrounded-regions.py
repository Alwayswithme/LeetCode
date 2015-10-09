#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-14 16:30:02
# Title      :  130 surrounded regions


#  Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# 
# For example,
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# After running your function, the board should be:
# 
# X X X X
# X X X X
# X X X X
# X O X X

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        row = len(board)
        col = len(board[0])
        if row < 2 or col < 2:
            return
        queue = []
        for i in range(row):
            queue.append((i, 0))
            queue.append((i, col - 1))
        for i in range(col):
            queue.append((0, i))
            queue.append((row - 1, i))
        while queue:
            i, j = queue.pop()
            if board[i][j] == 'O':
                board[i][j] = '#'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                        queue.append((x, y))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
