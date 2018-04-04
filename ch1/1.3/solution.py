
st= "how old are you             "


def urlify(s):
	flag=False
	temp=''
	for i in reversed(s):
		if i!=' ':
			flag=True
		if(i==' ' and flag==True) :
			temp+='02%'
		else:
			temp+=i
	
	return temp[::-1]
	

def urlify2(s):
	l = len(s)
	while s[l-1]==' ':
		l -= 1
	return s[:l].replace(' ', '%20')
	

			
print(urlify2(st))


	
