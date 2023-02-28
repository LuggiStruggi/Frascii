def catx(arr1, arr2, arr3):
    return [r1 + r2 + r3 for r1, r2, r3 in  zip(arr1, arr2, arr3)]

def caty(arr1, arr2, arr3):
    return arr1 + arr2 + arr3

def vicsek(n):
    if n == 0:
        return [["┼"]]
    c = vicsek(n-1)
    l = len(c)
    m = [[" " for _ in range(l)] for _ in range(l)]
    m = catx(m, c, m)
    c = catx(c, c, c)
    return caty(m, c, m)

def vicsek_string(n):
    return "\n".join("".join(s) for s in vicsek(n))

if __name__ == '__main__':
	print(vicsek_string(2))
