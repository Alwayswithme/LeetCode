#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2017-04-28 20:53:11
# Title      :  222 add and search word data structure design

#  Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
#
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
# Note:
# You may assume that all words are consist of lowercase letters a-z.

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            self.word[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if '.' not in word:
            return word in self.word[len(word)]
        for v in self.word[len(word)]:
            found = True
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    found = False
                    break
            if found:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
