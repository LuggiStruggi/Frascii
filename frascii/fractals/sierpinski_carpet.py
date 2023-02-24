def catx(arr1, arr2, arr3):
    return [r1 + r2 + r3 for r1, r2, r3 in  zip(arr1, arr2, arr3)]

def caty(arr1, arr2, arr3):
    return arr1 + arr2 + arr3

def sierpinski_carpet(n):
    if n == 0:
        return [["██"]]
    c = sierpinski_carpet(n-1)
    l = len(c)
    m = [["  " for _ in range(l)] for _ in range(l)]
    m = catx(c, m, c)
    c = catx(c, c, c)
    return caty(c, m, c)

def sierpinski_carpet_string(n):
    return "\n".join("".join(s) for s in sierpinski_carpet(n))

if __name__ == '__main__':
	print(sierpinski_carpet_string(3))
