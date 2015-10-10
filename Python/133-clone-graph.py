#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-19 16:21:26
# Title      :  133 clone graph


#  Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# 
# OJ's undirected graph serialization:
# 
# Nodes are labeled uniquely.
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# 
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# 
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
# 
#     First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
#     Second node is labeled as 1. Connect node 1 to node 2.
#     Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# 
# Visually, the graph looks like the following:
# 
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/


# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return node
        stack = [node]
        hash = {}
        copy = UndirectedGraphNode(node.label)
        hash[node] = copy
        while stack:
            ugn = stack.pop(0)
            for neighbor in ugn.neighbors:
                if neighbor not in hash:
                    hash[neighbor] = UndirectedGraphNode(neighbor.label)
                    stack.append(neighbor)
                hash[ugn].neighbors.append(hash[neighbor])
        return hash[node]
