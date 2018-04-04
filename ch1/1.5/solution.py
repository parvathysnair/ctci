s1='pale'
s2='tal'

def oneaway(s1,s2):
	flag=0
	#equal
	if s1 is s2:
		return True
	if abs(len(s1)-len(s2)) > 1:
		return False
	if abs(len(s1)-len(s2)) == 0:
		for i in range(0,len(s1)):
			if s1[i] != s2[i]:
				flag+=flag
		if flag >1:
			return False
		else:
			return True	
	if abs(len(s1)-len(s2)) == 1:
		for i in range(0,len(s2)):
			if s1[i] != s2[i]:
				return False
		return True
		
		
			
		
print(oneaway(s1,s2))	
		
