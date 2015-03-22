class AddressBook(object):
	def __init__(self):
		super(AddressBook, self).__init__()
		self.children = {}

	def addNode(self, node):
		self.children[node.getValue()] = node

	def nbElements(self):
		res = len(self.children)
		for _, node in self.children.iteritems():
			res += node.nbElements()
		return res

	def addPhone(self, phoneNumber):
		if len(phoneNumber) >= 1:
			firstDigit = phoneNumber[0]

			if firstDigit in self.children:
				self.children[firstDigit].addPhone(phoneNumber[1:])
			else:
				node = Node(firstDigit)
				node.addPhone(phoneNumber[1:])
				self.addNode(node)

class Node(object):
	def __init__(self, value):
		super(Node, self).__init__()
		self.children = {}
		self.value = value

	def getValue(self):
		return self.value

	def addNode(self, node):
		self.children[node.getValue()] = node

	def addPhone(self, phoneNumber):
		if len(phoneNumber) >= 1:
			firstDigit = phoneNumber[0]

			if firstDigit in self.children:
				self.children[firstDigit].addPhone(phoneNumber[1:])
			else:
				node = Node(firstDigit)
				node.addPhone(phoneNumber[1:])
				self.addNode(node)

	def nbElements(self):
		res = len(self.children)
		for _, node in self.children.iteritems():
			res += node.nbElements()
		return res

# The number of telephone numbers
N = int(raw_input())
addressBook = AddressBook()
for i in xrange(N):
	telephone = raw_input()
	addressBook.addPhone(telephone)

# The number of elements (referencing a number) stored in the structure.
print addressBook.nbElements()