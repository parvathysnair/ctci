def solution(n):
	a = 0
	b = 1
	while n:
		a, b = b, a+b
		n -= 1
	return a


def test_correctness(solutions):
	fp = open('output', 'r')
	for i, j in enumerate(solutions):
		ref = int(fp.readline())
		if ref == j:
			print('Test Case %s passed'%(i+1))
		else:
			print('Test Case %s failed'%(i+1))
	

if __name__=='__main__':
	fp = open('input', 'r')
	count = int(fp.readline())
	solutions = []
	for i in range(count):
		inp = int(fp.readline())
		solutions.append(solution(inp))
	test_correctness(solutions)
