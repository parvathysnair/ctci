#a="sdfhsjdfhh"


def uniqueChars(inp):
	if len(inp)>128: 
		return False
	artable = [False]*128
	for ch in inp:
		if artable[ord(ch)] is False:
			artable[ord(ch)]=True
		else:
			return False
	return True


def uniqueCharsDict(inp):
	dict1 = {}
	for i in inp:
		if i in dict1:
			return False
		else:
			dict1[i] = True
	return True
      
      
def uniqueCharsSet(inp):
	set1 = set()
	for i in inp:
		if i in set1:
			return False
		else:
			set1.add(i)
	return True

#print(uniqueChars(a))
	

if __name__=='__main__':
	fp = open('input','r')
	count = int(fp.readline())
	
	for i in range(count):
		input = fp.readline()
		print(uniqueChars(input))
