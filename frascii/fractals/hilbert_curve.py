def rot90(arr, direction):
	m = len(arr)
	n = len(arr[0])
	if direction == 'cw':
		return [[arr[m-1-j][i] for j in range(m)] for i in range(n)]
	elif direction == 'ccw':
		return [[arr[j][n-1-i] for j in range(m)] for i in range(n)]

def flipud(arr):
	return [row[::-1] for row in arr]

def catx(arr1, arr2):
	return [r1 + r2 for r1, r2 in zip(arr1, arr2)]

def caty(arr1, arr2):
	return arr1 + arr2

def add_value(arr, value):
    return [[elem + value for elem in row] for row in arr]

def hilbert_curve(n):
	if n == 1:
		return [[1, 2], [0, 3]]
	h = hilbert_curve(n-1)
	add = 4 ** (n-1)
	h_up = catx(add_value(h, add), add_value(h, 2*add))
	h_down = catx(flipud(rot90(h, 'ccw')), add_value(flipud(rot90(h, 'cw')), 3*add))
	h = caty(h_up, h_down)
	return h

def hilbert_curve_string(iterations):
	arr = hilbert_curve(iterations)
	out = ""
	n = len(arr)
	for i in range(n):
		for j in range(n):
			if i != 0 and i != n-1 and abs(arr[i-1][j] - arr[i][j]) == 1 and abs(arr[i+1][j] - arr[i][j]) == 1:
				out += "│ "
			elif j != 0 and j != n-1 and abs(arr[i][j-1] - arr[i][j]) == 1 and abs(arr[i][j+1] - arr[i][j]) == 1:
				out += "──"
			elif j != 0 and i != n-1 and abs(arr[i][j-1] - arr[i][j]) == 1 and abs(arr[i+1][j] - arr[i][j]) == 1:
				out += "┐ "
			elif j != 0 and i != 0 and abs(arr[i][j-1] - arr[i][j]) == 1 and abs(arr[i-1][j] - arr[i][j]) == 1:
				out += "┘ "
			elif i != 0 and j != n-1 and abs(arr[i-1][j] - arr[i][j]) == 1 and abs(arr[i][j+1] - arr[i][j]) == 1:
				out += "└─"
			elif i != n-1 and j != n-1 and abs(arr[i+1][j] - arr[i][j]) == 1 and abs(arr[i][j+1] - arr[i][j]) == 1:
				out += "┌─"
			else:
				out += "│ " if iterations % 2 else "──"
			if j == n-1:
				out = out[:-1] + "\n"
	return out[:-1]

if __name__ == '__main__':
	print(hilbert_curve_string(3))
