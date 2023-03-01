def catx(arr1, arr2, arr3):
 	return [r1 + r2 + r3 for r1, r2, r3 in zip(arr1, arr2, arr3)]

def caty(arr1, arr2, arr3, arr4):
 	return arr1 + arr2 + arr3 + arr4

# apologies for this :D
def shorten_middle(curve):
	new = [[curve[i][j] if j < len(row)//3 or j >= 2*len(row)//3 else
	((curve[i-len(curve)//14][j] if i >= len(curve)//14 else " ") if i < len(curve)//2 else curve[i+len(curve)//14][j] if i < len(curve) - len(curve)//14 else " ")
	for j, c in enumerate(row)] for i, row in enumerate(curve)]
	return new[len(curve)//14:-len(curve)//14]

def empty(curve):
	return [[" "]*len(row) for row in curve]

def filled(curve):
	return [["█"]*len(row) for row in curve]

def upper(curve):
	return [row for i, row in enumerate(curve) if i < 3*len(curve)//4]

def lower(curve):
	return [row for i, row in enumerate(curve) if i >= len(curve)//4]

def right_up(curve):
	return [["█" if j < len(row)//2 else c for j, c in enumerate(row)] if i >= len(curve)//4 else row for i, row in enumerate(curve)]

def left_down(curve):
	return [["█" if j > len(row)//2-1 else c for j, c in enumerate(row)] if i < 3*len(curve)//4 else row for i, row in enumerate(curve)]

def right_down(curve):
	return [["█" if j < len(row)//2 else c for j, c in enumerate(row)] if i < 3*len(curve)//4 else row for i, row in enumerate(curve)]

def left_up(curve):
	return [["█" if j > len(row)//2-1 else c for j, c in enumerate(row)] if i >= len(curve)//4 else row for i, row in enumerate(curve)]


def koch(n):
	if n == 0:
		return [["◢◣"]]
	elif n == 1:
		return [[" ", " ","◢", "◣", " ", " "], ["◥", "█", "█", "█", "█", "◤"],["◢", "█", "█", "█", "█", "◣"], [" ", " ", "◥", "◤", " ", " "]]
	else:
		k = koch(n-1)
		f = filled(k)
		e = empty(k)
		u = catx(e, upper(k), e)
		m1 = catx(left_up(k), f, right_up(k))
		m2 = catx(left_down(k), f, right_down(k))
		l = catx(e, lower(k), e)
		k = caty(u, m1, m2, l)
		k = shorten_middle(k)
	return k

def koch_string(n):
	return "\n".join("".join(row) for row in koch(n))

if __name__ == "__main__":
	print(koch_string(2))
