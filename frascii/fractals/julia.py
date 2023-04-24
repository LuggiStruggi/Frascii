def in_julia(f, z_0, max_iter):
	z = z_0
	for i in range(max_iter):
		z = f(z)
		if abs(z) >= 2:
			return i
	return max_iter

def julia_string(f, x, y, x_radius, y_radius, stepsize, max_iter, style, grid):
	fz = eval(f"lambda z: {f.replace('i', 'j')}")

	try:
		fz(0.5)
	except:
		raise ValueError(f"The given function f(z) = {f} is not a proper input.")

	if grid == "rect":
		mset = [[in_julia(fz, complex(x + dx * stepsize, y - dy * stepsize * 2), max_iter)
				for dx in range(-x_radius, x_radius+1)] for dy in range(-y_radius, y_radius+1)]
		if style == "non-repeating":
			chars = [' ', '░', '▒', '▓', '█']
			return '\n'.join(''.join(chars[int(4*d/max_iter)] for d in l) for l in mset)
		elif style == "repeating":
			chars = ['░', '▒', '▓', '▒']
			m = len(chars)
			return '\n'.join(''.join(' ' if d < 1 else chars[d%m] if d < max_iter else '█' for d in l) for l in mset)
	
	elif grid == "square":
		mset = [[in_julia(fz, complex(x + dx * stepsize, y - dy * stepsize), max_iter)
				for dx in range(-x_radius, x_radius+1)] for dy in range(-y_radius, y_radius+1)]
		if style == "non-repeating":
			chars = [' ', '░', '▒', '▓', '█']
			return '\n'.join(''.join(chars[int(4*d/max_iter)]*2 for d in l) for l in mset)
		elif style == "repeating":
			chars = ['░', '▒', '▓', '▒']
			m = len(chars)
			return '\n'.join(''.join('  ' if d < 1 else chars[d%m]*2 if d < max_iter else '██' for d in l) for l in mset)
	

if __name__ == '__main__':
	f = "z**2 - 0.4 + 0.6j"
	print(julia_string(f, 0, 0, 12*15, 12*15, 0.05/8, 40, grid="square", style="non-repeating"))
