#partition=5

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

	
	def partition(self,p):
		#when pivot is present
		temp=self.head
		while temp is not None:
			if temp.data<p:
				temp=temp.next
			elif temp.data==p:
				if temp.data>temp.next.data :
					#swap
					t=temp
					temp=temp.next
					temp.next=t
				temp=temp.next
			else:
				if temp.data>temp.next.data :
					#swap
					t=temp
					temp=temp.next
					temp.next=t
				temp=temp.next
		return



if __name__=='__main__':
	#creating instance of node
	n1=node(13)
	n2=node(5)
	n3=node(8)
	n4=node(5)
	n5=node(10)
	n6=node(2)
	n7=node(1)
	
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
	
	sll.partition(5)
	print("updated list")
	sll.print_items()
	
