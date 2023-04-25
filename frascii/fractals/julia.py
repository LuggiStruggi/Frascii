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


def julia_explore(f, x, y, x_radius, y_radius, stepsize, max_iter, style="repeating", grid="rect"):
	
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
		nonlocal f
		styles = ["non-repeating", "repeating"]
		si = 0 if style == "non-repeating" else 1
 	
		while True:
			stdscr.clear()
			rows, cols = stdscr.getmaxyx()
			y_rad = min(y_radius, rows//2-1)
			x_rad = min(x_radius, cols//(2 if grid == "rect" else 4)-1)
			stdscr.addstr(0, 0, julia_string(f, x, y, x_rad, y_rad, s, i, styles[si], grid))
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
			elif key == ord('h'):
				stdscr.clear()
				stdscr.addstr(0, 0, ("CONTROLS:\n\nARROWS       : navigate complex plane\nPAGE-UP/DOWN : zoom in/out\n',' and '.'  :")+
									(" change max-iterations\n'-'          : change style\nESC and 'x'  : leave explore mode and print to screen.\n\n")+
									(f"CURRENT COMMAND:\nfrascii julia -x {x} -y {y} -x_radius {x_rad} -y_radius {y_rad} -stepsize {s}")+
									(f" -max_iter {i} -style {styles[si]} -grid {grid}"))
				curses.flushinp()
				while stdscr.getch() not in (ord('h'), ord('x'), 27):
					pass

		return x, y, x_rad, y_rad, s, i, styles[si], grid

	args = wrapper(main)
	curses.endwin()
	return args

if __name__ == '__main__':
	f = "z**2 - 0.4 + 0.6j"
	julia_explore(f, 0, 0, 12*15, 12*15, 0.05/8, 40, grid="square", style="non-repeating")
