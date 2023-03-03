def cantor_string(n):
	out = ["▄"*3**n]
	while n >= 1:
		len_old = 3**n
		len_new = 3**(n-1)
		new = out[-1].replace("▄"*len_old, "▄"*len_new + " "*len_new + "▄"*len_new)
		out.append(new)
		n -= 1
	return "\n".join("".join(row) for row in out)

if __name__ == '__main__':
	print(cantor_string(2))
