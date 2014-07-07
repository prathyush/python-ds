#
# A basic implementation of a Trie.
#

class Trie:
	#
	# Node representing a trie node.
	#
	class TrieNode:
		def __init__(self, name, parent=None):
			self.name = name;
			self.value = None;
			self.parent = parent;
			self.children = {};
		
		def isLeaf(self):
			if self.value: return True;
			return False;

		def setLeaf(self, value):
			self.value = value;

		def getValue(self):
			return self.value;

		def __repr__(self):
			return self.name;

	def __init__(self):
		self.root = Trie.TrieNode('root');

	def insert(self, word, value):
		node = self.root;
		
		i, node, found = self.getLastMatch(word);

		if found and node.isLeaf():
			# Duplicate
			print 'Duplicate';
			return None;
		elif found:
			print 'Matched';
			node.setLeaf(value);
			return;

		# Add the rest of the trie
		for j in range(i, len(word)-1):
			node.children[word[j]] = Trie.TrieNode(word[j], node);
			node = node.children[word[j]];

		# Mark the last node as leaf and add it's value.
		node.setLeaf(value)
	
	def getLastMatch(self, word):
		node = self.root;
		found = False;

		for i in range(len(word)):
			if node.children.has_key(word[i]):
				node = node.children[word[i]];
			else:
				break;

		if i == len(word)-1:
			found = True;

		return i, node, found;

	def search(self, word):
		print 'Searching for %s' % (word);

		i, node, found = self.getLastMatch(word);

		# Not a complete match.
		if found and node.isLeaf():
			return node.getValue();
		else:
			return None;

	def remove(self, word):
		i, node, found = self.getLastMatch(word);

		if not found:
			return None;

		for i in range(len(word)):
			if len(node.parent.children) > 1:
				if node.parent.children.pop(node.name, None):
					break;
				else:
					return; # Key not found, shouldn't happen.
			else: 
				# Just one child, lets move up.
				node = node.parent;


if __name__ == '__main__':

	trie = Trie();
	
	trie.insert('apple', 'fruit');
	trie.insert('air', 'gas');
	trie.insert('app', 'utility');
	trie.insert('applets', 'java');
	trie.insert('ap', 'state');

	print trie.search('app');
	print trie.search('air');
	print trie.search('ap');
	print trie.search('cat');
	
	trie.remove('ap');
	print trie.search('ap');
	trie.insert('ap', 'old state');
	print trie.search('ap');
	trie.insert('ap', 'new state');
