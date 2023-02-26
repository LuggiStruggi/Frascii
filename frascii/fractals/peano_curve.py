def rot90(arr, direction):
	m = len(arr)
	n = len(arr[0])
	if direction == 'cw':
		return [[arr[m-1-j][i] for j in range(m)] for i in range(n)]
	elif direction == 'ccw':
		return [[arr[j][n-1-i] for j in range(m)] for i in range(n)]

def fliplr(arr):
	return [row[::-1] for row in arr]

def flipud(arr):
	return [row for row in arr[::-1]]

def catx(arr1, arr2, arr3):
	return [r1 + r2 + r3 for r1, r2, r3 in zip(arr1, arr2, arr3)]

def caty(arr1, arr2, arr3):
	return arr1 + arr2 + arr3

def add_value(arr, value):
    return [[elem + value for elem in row] for row in arr]

def peano_curve(n):
	if n == 1:
		return [[2, 3, 8], [1, 4, 7], [0, 5, 6]]
	hlu = peano_curve(n-1)
	hru = fliplr(hlu)
	hld = flipud(hlu)
	hrd = flipud(hru)
	add = 9 ** (n-1)
	h_up = catx(add_value(hlu, 2*add), add_value(hld, 3*add), add_value(hlu, 8*add))
	h_mid = catx(add_value(hru, 1*add), add_value(hrd, 4*add), add_value(hru, 7*add))
	h_down = catx(hlu, add_value(hld, 5*add), add_value(hlu, 6*add))
	h = caty(h_up, h_mid, h_down)
	return h

def peano_curve_string(iterations):
	arr = peano_curve(iterations)
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
				out += "│ " if iterations % 9 else "──"
			if j == n-1:
				out = out[:-1] + "\n"
	return out[:-1]

if __name__ == '__main__':
	print(peano_curve_string(2))
