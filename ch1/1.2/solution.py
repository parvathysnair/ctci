#s1='bad'
#s2='dbas'

def sorting(str):
	"""
	O(Nlog(n))
	"""
	a=''.join(sorted(str))
	return a


def checkperm(s1,s2):
	"""
	O(N)
	"""
	if s1 == s2:
		return True
	else: 
		return False


def checkpermdict(s1, s2):
	dict1 = {}
	
	for i in s1:
		if i in dict1:
			dict1[i] += 1
		else:
			dict1[i] = 1

	for i in s2:
		if i in dict1:
			dict1[i] -= 1
			if dict1[i] == 0:
				del dict1[i]
		else:
			return False

	if len(dict1) > 0:
		return False

	return True



#print(sorting(s1))
#print(sorting(s2))


if __name__== '__main__':
	fp=open('input','r')
	s1=fp.readline()
	s2=fp.readline()
	a=sorting(s1)
	b=sorting(s2)
	print(checkperm(a,b))
