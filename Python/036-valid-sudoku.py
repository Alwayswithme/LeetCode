#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-20 15:20:03
# Title      :  36 valid sudoku

# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# 
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# 
# 
# A partially filled sudoku which is valid.
# 
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        for i in range(9):
            if not self.isValidList([board[i][j] for j in range(9)]) or not self.isValidList([board[j][i] for j in range(9)]):
                return False
        for i in range(3):
            for j in range(3):
                if not self.isValidList([board[k][l] for l in range(3 * j, 3 * j + 3) for k in range(3 * i, 3 * i + 3)]):
                    return False
        return True
    def isValidList(self, xs):
        xs = filter(lambda x: x != '.', xs)
        return len(set(xs)) == len(xs)
