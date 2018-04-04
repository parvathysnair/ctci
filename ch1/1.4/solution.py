inputstr='tact'

def palinperm(s):
	dict1 = {}
	for i in s:
		if i == ' ' :
			continue
		if i in dict1:
			dict1[i] -= 1
			if dict1[i] == 0:
				del dict1[i]
		else: 
			dict1[i] = 1
				
	if (sum(dict1.values()) == 0 or sum(dict1.values())==1):
		return True
	else:
		return False
	
	
	
def palinpermset(s):
	strset=set()
	for i in s:
		if i ==' ':
			continue
		if i in strset:
			strset.remove(i)
		else:
			strset.add(i)
	
	if len(strset)>1:
		return False
	else: 
		return True
	
	
	
if __name__ == '__main__':
	#print(palinperm(inputstr))
	print(palinpermset(inputstr))
