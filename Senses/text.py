
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Text/Strings sense/module for Sofia
'''

from collections import deque

class VerbalMemoryNode(object):
	__slots__ = ['value','children']

	def __init__(self, value):
		self.value = value
		self.children = {}

class VerbalMemory(object):
	def __init__(self):
		self.root = VerbalMemoryNode(None)

	def add(self, s):
		current = self.root
		for c in s:
			print c
			if c in current.children:
				current = current.children[c]
			else:
				new_node = VerbalMemoryNode(c)
				print new_node.value
				current.children[c] = new_node
				current = new_node
		if None not in current.children:
			current.children[None] = None

	def contains(self, s):
		current = self.root
		for c in s:
			if c in current.children:
				current = current.children[c]
			else:
				return False
		return None in current.children

	def starts_with(self, prefix):
		current = self.root
		for c in prefix:
			if c in current.children:
				current = current.children[c]
			else:
				return []
		results = []
		nodes = deque([(current, prefix)])
		while nodes:
			node, prefix = nodes.pop()
			for key, child in node.children.items():
				if key is None:
					results.append(prefix)
				else:
					nodes.append((child, prefix + key))
		return results
