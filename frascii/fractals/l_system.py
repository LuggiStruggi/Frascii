import time
import importlib.util

def l_system(start, rules, n):
	letters = start
	rules = rules.replace("(", "").replace(")", "").replace(" ", "").split(",")
	rules = dict(rule.split("->") for rule in rules)
	for i in range(n):
		letters = "".join(rules[l] if l in rules else l for l in letters)
	return "".join(l for l in letters if l in "+-Ff[]")
	

def cleanup(arr):
	if all(seg == "  " for seg in arr[0]):
		arr = arr[1:]
	if all(seg == "  " for seg in arr[-1]):
		arr = arr[:-1]
	if all(row[0] == "  " for row in arr):
		arr = [row[1:] for row in arr]
	if all(row[-1] == "  " for row in arr):
		arr = [row[:-1] for row in arr]
	return arr

def l_system_string(start, rules, n, start_dir="U"):
	
	letters = l_system(start, rules, n)

	out, pos_stack, pos, comp = init_grid(start_dir)

	for i, turn in enumerate(letters):
		
		out, pos_stack, pos = resize_grid(out, pos_stack, pos)
		
		out, pos_stack, pos, comp = grid_command(out, pos_stack, pos, comp, turn)	
	
	out, pos_stack, pos = resize_grid(out, pos_stack, pos)

	return grid_to_string(out)


def init_grid(start_dir="U"):
	
	grid = [["URDL"]]
	pos = [0, 0]  #y, x
	stack = []
	head = "URDL"
	if start_dir not in "URDL":
		raise ValueError(f"start_dir must be U,R,D or L but was {start_dir}")
	while head[0] != start_dir:
		head = head[1:] + head[0]
	
	return grid, stack, pos, head

def grid_to_string(grid):
	trans = {"URDL": "  ", "URD": "╴ ", "URL": "╷ ", "UDL": "╶─",
			 "RDL": "╵ ", "RL": "│ ", "UD": "──", "UR": "┐ ",
			 "UL": "┌─", "RD": "┘ ", "DL": "└─", "U": "┬─",
			 "R": "┤ ", "D": "┴─", "L": "├─", "": "┼─"}
	return "\n".join("".join(trans[c] for c in row) for row in cleanup(grid))


def resize_grid(grid, stack, pos):

	if pos[0] == len(grid) - 1:
		grid.append(["URDL" for i in range(len(grid[0]))])
	if pos[1] == len(grid[0]) - 1:
		grid = [row + ["URDL"] for row in grid]
	if pos[0] == 0:
		grid.insert(0, ["URDL" for i in range(len(grid[0]))])
		pos[0] = 1
		stack = [[[p[0][0]+1, p[0][1]], p[1]] for p in stack]
	if pos[1] == 0:
		grid = [["URDL"] + row for row in grid]
		pos[1] = 1	
		stack = [[[p[0][0], p[0][1]+1], p[1]] for p in stack]
	return grid, stack, pos


def grid_command(grid, stack, pos, head, cmd):
	
	curr = grid[pos[0]][pos[1]]
	if cmd == "-":
		head = head[1:] + head[0]

	elif cmd == "+":
		head = head[-1] + head[:-1]

	elif cmd in "fF":
		if cmd == "F":
			grid[pos[0]][pos[1]] = curr.replace(head[0], "")
		prev_head = head
		if head[0] == "U":
			pos[0] -= 1
		elif head[0] == "R":
			pos[1] += 1
		elif head[0] == "D":
			pos[0] += 1
		elif head[0] == "L":
			pos[1] -= 1
		if cmd == "F":
			grid[pos[0]][pos[1]] = grid[pos[0]][pos[1]].replace(head[2], "")

	elif cmd == "[":
		stack.append([[pos[0], pos[1]], head])

	elif cmd == "]":
		pos, head = stack.pop()

	return grid, stack, pos, head


def l_system_animate(start, rules, n, start_dir="U", speed=0.3):

	if importlib.util.find_spec('curses') is None:
		raise Exception("To use the explore command the curses package must be installed.")
	
	import curses
	from curses import wrapper
	stdscr = curses.initscr()
	letters = l_system(start, rules, n)
	curses.noecho()
	curses.cbreak()
	stdscr.nodelay(True)
	stdscr.keypad(True)
	
	def main(stdscr):
		nonlocal letters
		nonlocal start_dir
		nonlocal speed

		out, pos_stack, pos, comp = init_grid(start_dir)

		for i, turn in enumerate(letters):
		
			key = stdscr.getch()
			curses.flushinp()
			if key == ord('x') or key == 27:
				return grid_to_string(out)

			rows, cols = stdscr.getmaxyx()
			if len(out) >= rows or len(out[0]) >= cols:
				return grid_to_string(out)
 
			out, pos_stack, pos = resize_grid(out, pos_stack, pos)

			stdscr.addstr(0, 0, grid_to_string(out))
			stdscr.refresh()
			time.sleep(speed)	
			
			out, pos_stack, pos, comp = grid_command(out, pos_stack, pos, comp, turn)
		
		out, pos_stack, pos = resize_grid(out, pos_stack, pos)

		return grid_to_string(out)

	s = wrapper(main)
	curses.endwin()
	return s

if __name__ == '__main__':
	print(l_system_animate("A", "(A->+BF-AFA-FB+),(B->-AF+BFB+FA-)", 5, "U", 0.003))
