
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


#delete middle node
	def delmiddle(self):
		count=0
		temp=self.head
		
		while temp is not None:
			count+=1
			temp=temp.next
		#print(count)
		
		if count>2:
			index=int(round(count/2))
			#print(index)
		else:
			return False
		
		t1=self.head
		t2=t1.next
		i=1
		while t2 is not None:
			i+=1
			if i==index:
				t1.next=t2.next
				return True
			t2=t2.next
			t1=t1.next
		return False
			
			
		




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
	
	if sll.delmiddle()==True:
		print("updated list")
		sll.print_items()
	else:
		print("Not more than 2 elements")
		sll.print_items()
	
	
	
	
	
	
