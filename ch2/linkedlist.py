class node:
	def __init__(self,data):
		self.data=data
		self.next=None
		return
	
	def check(self,value):
		if self.data==value:
			return True
		else:
			False
	

#creating instance of node
n1=node(10)
n2=node(15)
n3=node(20)



class slinkedlist:
	def __init__(self):
		self.head=None
		self.tail=None
#add	
	def add_item(self,item):		
		if not isinstance(item,node):
			item= node(item);
	
		if self.head is None:
			self.head=item
		else:
			self.tail.next=item
		
		self.tail=item


sll=slinkedlist()
sll.add_item(n1)

