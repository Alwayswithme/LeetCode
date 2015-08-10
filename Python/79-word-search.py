#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-08-10 20:09:52
# Title      :  79 word search

#  Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# 
# For example,
# Given board =
# 
# [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
# 
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if not word:
            return False
        if len(board) * len(board[0]) < len(word):
            return False
        used = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, used, 0, i, j):
                    return True
        return False
    
    def search(self, board, word, used, index, i, j):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        if used[i][j] or board[i][j] != word[index]:
            return False
        used[i][j] = True
        index += 1
        result = (self.search(board, word, used, index, i + 1, j)
                or self.search(board, word, used, index, i, j + 1)
                or self.search(board, word, used, index, i - 1, j)
                or self.search(board, word, used, index, i, j - 1))
        used[i][j] = False
        return result
