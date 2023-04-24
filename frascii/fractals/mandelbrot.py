
def in_mandelbrot(c, max_iter):
	z = 0
	for i in range(max_iter):
		z = z**2 + c
		if abs(z) >= 2:
			return i
	return max_iter

def mandelbrot_string(x, y, x_radius, y_radius, stepsize, max_iter, style="repeating", grid="square"):
	if grid == "rect":
		mset = [[in_mandelbrot(complex(x + dx * stepsize, y - dy * stepsize * 2), max_iter)
				for dx in range(-x_radius, x_radius+1)] for dy in range(-y_radius, y_radius+1)]
		
		if style == "repeating":
			shades = ['░', '▒', '▓', '▒']
			m = len(shades)
			return '\n'.join(''.join(" " if d == 0 else shades[d%m] if d < max_iter else "█" for d in l) for l in mset)

		elif style == "non-repeating":
			shades = [' ', '░', '▒', '▓', '█']
			return '\n'.join(''.join(shades[int(4*d/max_iter)] for d in l) for l in mset)

	elif grid == "square":
		mset = [[in_mandelbrot(complex(x + dx * stepsize, y - dy * stepsize), max_iter)
				for dx in range(-x_radius, x_radius+1)] for dy in range(-y_radius, y_radius+1)]
		if style == "repeating":
			shades = ['░', '▒', '▓', '▒']
			m = len(shades)
			return '\n'.join(''.join("  " if d == 0 else shades[d%m]*2 if d < max_iter else "██" for d in l) for l in mset)

		elif style == "non-repeating":
			shades = [' ', '░', '▒', '▓', '█']
			return '\n'.join(''.join(shades[int(4*d/max_iter)]*2 for d in l) for l in mset)

if __name__ == '__main__':
	import curses
	from curses import wrapper
	stdscr = curses.initscr()
	#curses.use_default_colors()	
	curses.mousemask(1)
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)

	def main(stdscr):
		x = -0.8
		y = 0
		s = 0.05
		i = 20

		# Clear screen
		while True:
			stdscr.clear()
			rows, cols = stdscr.getmaxyx()
			y_radius = rows//2-1
			x_radius = cols//2-1
			stdscr.addstr(0, 0, mandelbrot_string(x, y, x_radius, y_radius, s, i, "repeating"))
			stdscr.refresh()
			key = stdscr.getch()
			curses.flushinp()
			if key == curses.KEY_RIGHT:
				x += 5*s
			if key == curses.KEY_LEFT:
				x -= 5*s
			if key == curses.KEY_UP:
				y += 5*s
			if key == curses.KEY_DOWN:
				y -= 5*s
			if key == curses.KEY_NPAGE:
				s /= 2
			if key == curses.KEY_PPAGE:
				s *= 2
			if key == ord(','):
				i -= 1
				i = max(i,1)
			if key == ord('.'):
				i += 1
			if key == curses.KEY_MOUSE:
				_, mx, my, _, _ = curses.getmouse()
				x += (mx - x_radius)*s
				y += (-my + y_radius)*s
			
	wrapper(main)

