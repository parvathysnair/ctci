
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
#print
	def print_items(self):
		temp=self.head
		
		while temp is not None:
			print(temp.data)
			temp=temp.next
		return

#remove dups
	def remove_dupe(self):
		temp1=self.head
		temp2=self.head
		while temp1 is not None:
			check=temp1.next
			while check is not None:
				if temp1.data == check.data:
					if check.next is not None:
						temp2.next = check.next
					else:
						temp2.next=None
						
					check=check.next
				else:
					if check is not None:
						check=check.next
						temp2=temp2.next
					else:
						check=None
			temp1=temp1.next
			temp2=temp1


if __name__=='__main__':
	#creating instance of node
	n1=node(10)
	n2=node(15)
	n3=node(20)
	n4=node(15)
	n5=node(12)
	n6=node(10)
	
	#adding nodes to list	
	sll=slinkedlist()
	sll.add_item(n1)
	sll.add_item(n2)
	sll.add_item(n3)
	sll.add_item(n4)
	sll.add_item(n5)
	sll.add_item(n6)
	
	print("orginal list")
	sll.print_items()
	
	sll.remove_dupe()
	
	print("Dups removed list")
	sll.print_items()
	
	
	
	
