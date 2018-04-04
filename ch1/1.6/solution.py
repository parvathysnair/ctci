s='ppfffffgg'

def compression(s):
	dic1={}
	st=''
	for i in s:
		if i in dic1:
			dic1[i] +=1
		else:
			dic1[i]=1
	for key, value in dic1.items():
		st=st+str(key)+str(value)
	if len(st) < len(s):	
		print(st)
	else:
		print(s)
	
	#print(dic1.keys())	
			
			
			
#second method
def compression1(s):
	dic1={}
	st=''
	for i in s:
		if i in dic1:
			dic1[i] +=1
		else:
			dic1[i]=1
	for key, value in dic1.items():
		st=st+str(key)+str(value)
	if len(st) < len(s):	
		print(st)
	else:
		print(s)




compression1(s)
