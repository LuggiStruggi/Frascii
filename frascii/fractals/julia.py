def in_julia(f, z_0, max_iter):
	z = z_0
	for i in range(max_iter):
		z = f(z)
		if abs(z) >= 2:
			return i
	return max_iter

def julia_string(f, x, y, x_radius, y_radius, stepsize, max_iter):
	fz = eval(f"lambda z: {f.replace('i', 'j')}")

	try:
		fz(0.5)
	except:
		raise ValueError(f"The given function f(z) = {f} is not a proper input.")

	mset = [[int(4*in_julia(fz, complex(x + dx * stepsize, y - dy * stepsize * 2), max_iter) / max_iter)
			for dx in range(-x_radius, x_radius+1)] for dy in range(-y_radius, y_radius+1)]
	chars = [' ', '░', '▒', '▓', '█']
	return '\n'.join(''.join(chars[d] for d in l) for l in mset)

if __name__ == '__main__':
	f = "z**2 - 0.4 + 0.6j"
	print(julia_string(f, 0, 0, 30*15, 12*15, 0.05/15, 40))
