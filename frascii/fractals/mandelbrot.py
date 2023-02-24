def in_mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) >= 2:
            return i
    return max_iter

def mandelbrot_string(x, y, x_radius, y_radius, stepsize, max_iter):
    mset = [[int(4*in_mandelbrot(complex(x + dx * stepsize, y - dy * stepsize * 2), max_iter) / max_iter)
			for dx in range(-x_radius, x_radius+1)] for dy in range(-y_radius, y_radius+1)]
    chars = [' ', '░', '▒', '▓', '█']
    return '\n'.join(''.join(chars[d] for d in l) for l in mset)

if __name__ == '__main__':
	print(mandelbrot_string(-0.8, 0, 27, 12, 0.05, 20))
