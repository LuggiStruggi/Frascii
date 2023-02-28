def sierpinski_triangle_string(n):
	p = pascal(n)
	l = len(p)
	return "\n".join((l-i)*" "+"".join("◢◣" if e % 2 else "  " for e in row) for i, row in enumerate(p))

def pascal(n):
	p = [[1]]
	for i in range(1, 2**n):
		row = []
		for j in range(1, i):
			row.append(p[-1][j-1]+p[-1][j])
		p.append([1] + row + [1])
	return p

if __name__ == '__main__':
	print(sierpinski_triangle_string(3))
