#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-13 16:08:28
# Title      :  127 word ladder


#  Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
# 
#     Only one letter can be changed at a time
#     Each intermediate word must exist in the word list
# 
# For example,
# 
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# 
# Note:
# 
#     Return 0 if there is no such transformation sequence.
#     All words have the same length.
#     All words contain only lowercase alphabetic characters.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        distance, queue = 0, [beginWord]
        wordList.add(endWord)
        while queue:
            next = []
            for word in queue:
                if word == endWord:
                    return distance + 1
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if word != candidate and candidate in wordList:
                            next.append(candidate)
                            wordList.remove(candidate)
            queue = next
            distance += 1
        return 0
