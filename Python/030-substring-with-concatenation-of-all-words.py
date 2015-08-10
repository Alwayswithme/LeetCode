#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-22 12:34:13
# Title      :  30 substring with concatenation of all words

# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
# 
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
# 
# You should return the indices: [0,9].
# (order does not matter). 

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        result, word_map, word_num, word_len = [], {}, len(words), len(words[0])
        for i in words:
            if i not in word_map:
                word_map[i] = 1
            else:
                word_map[i] += 1
        for i in range(word_len):
            current_map, left = {}, i
            for j in range(i, len(s), word_len):
                sub_str = s[j:j + word_len]
                if sub_str in word_map:
                    if sub_str not in current_map:
                        current_map[sub_str] = 1
                    else:
                        current_map[sub_str] += 1
                    if current_map[sub_str] > word_map[sub_str]:
                        while True:
                            temp = s[left:left + word_len]
                            current_map[temp] -= 1
                            left += word_len
                            if temp == sub_str:
                                break
                    if sum(current_map.values()) == word_num:
                        # find a match substring, mark the index and find more
                        result.append(left)
                        temp = s[left:left + word_len]
                        current_map[temp] -= 1
                        left += word_len
                else:
                    #start over
                    current_map, left = {}, j + word_len
        return result
