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

def mandelbrot_explore(x, y, x_radius, y_radius, stepsize, max_iter, style="repeating", grid="rect"):
	
	import curses
	from curses import wrapper
	stdscr = curses.initscr()
	curses.mousemask(1)
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)
	s = stepsize
	i = max_iter

	def main(stdscr):
		nonlocal x
		nonlocal y
		nonlocal x_radius
		nonlocal y_radius
		nonlocal s
		nonlocal style
		nonlocal grid
		nonlocal i
		styles = ["non-repeating", "repeating"]
		si = 0 if style == "non-repeating" else 1
 	
		while True:
			stdscr.clear()
			rows, cols = stdscr.getmaxyx()
			y_rad = min(y_radius, rows//2-1)
			x_rad = min(x_radius, cols//(2 if grid == "rect" else 4)-1)
			stdscr.addstr(0, 0, mandelbrot_string(x, y, x_rad, y_rad, s, i, styles[si], grid))
			stdscr.refresh()
			key = stdscr.getch()
			curses.flushinp()
			if key == curses.KEY_RIGHT:
				x += 5*s
			elif key == curses.KEY_LEFT:
				x -= 5*s
			elif key == curses.KEY_UP:
				y += 5*s
			elif key == curses.KEY_DOWN:
				y -= 5*s
			elif key == curses.KEY_NPAGE:
				s /= 2
			elif key == curses.KEY_PPAGE:
				s *= 2
			elif key == ord(','):
				i -= 1
				i = max(i,1)
			elif key == ord('.'):
				i += 1
			elif key == ord('-'):
				si = 1 - si
			elif key == curses.KEY_MOUSE:
				_, mx, my, _, _ = curses.getmouse()
				x += ((mx if grid == "rect" else mx//2) - x_rad)*s
				y += (-my + y_rad)*s
			elif key == 27 or key == ord('x'):
				break

		return x, y, x_rad, y_rad, s, i, styles[si], grid

	args = wrapper(main)
	curses.endwin()
	return args

if __name__ == '__main__':
	mandelbrot_explore(x=-0.8, y=0, x_radius=4000, y_radius=4000, stepsize=0.05, max_iter=20)
