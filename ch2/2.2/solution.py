k=2



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

#remove k-th element to last
	def returntolast(self,k):	
		flag=None
		count=1
				
		if k==1:
			flag=self.head
			self.head=self.head.next
		else:
			temp1=self.head
			temp2=temp1.next
		
			while temp2 is not None:
				count+=1
				if count==k:
					flag=temp2 #"flag is now the k-th element"
					temp1.next=temp2.next
					break
				else:
					temp2=temp2.next			
					temp1=temp1.next
					
		if flag is not None:
			temp1=self.head
			while temp1.next is not None:
				temp1=temp1.next
			temp1.next=flag
			flag.next=None
			return True
		else:
			return True
					
		

if __name__=='__main__':
	#creating instance of node
	n1=node(10)
	n2=node(15)
	n3=node(20)
	n4=node(25)
	n5=node(1)
	n6=node(0)
	
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
	
	if sll.returntolast(k)==True:
		print("updated list")
		sll.print_items()
	else:
		print("The is no k-th element")
	
	
	
