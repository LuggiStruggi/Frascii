def dragon_curve_letters(n):
	if n == 0:
		return ""
	else:
		prev = dragon_curve_letters(n-1)
		flip = "".join("R" if l == "L" else "L" for l in prev)[::-1]
		return prev + "R" + flip

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

def dragon_curve_string(n):
	if n == 0:
		return "│ "
	letters = dragon_curve_letters(n)
	out = [["  "], ["╵ "]]
	pos = [1, 0]  #y, x
	head = 0
	
	for i, turn in enumerate(letters):
		
		# Enlarge grid
		if pos[0] == len(out) - 1:
			out.append(["  " for i in range(len(out[0]))])
		if pos[1] == len(out[0]) - 1:
			out = [row + ["  "] for row in out]
		if pos[0] == 0:
			out.insert(0, ["  " for i in range(len(out[0]))])
			pos[0] = 1
		if pos[1] == 0:
			out = [["  "] + row for row in out]
			pos[1] = 1
		
		# up	
		if head == 0:
			pos[0] -= 1
			if turn == "R":
				head = 1
				out[pos[0]][pos[1]] = ("┌─" if out[pos[0]][pos[1]] == "  " else "┼─")

			elif turn == "L":
				head = 3
				out[pos[0]][pos[1]] = ("┐ " if out[pos[0]][pos[1]] == "  " else "┼─")
		
		# right
		elif head == 1:
			pos[1] += 1
			if turn == "R":
				head = 2
				out[pos[0]][pos[1]] = ("┐ " if out[pos[0]][pos[1]] == "  " else "┼─")

			elif turn == "L":
				head = 0
				out[pos[0]][pos[1]] = ("┘ " if out[pos[0]][pos[1]] == "  " else "┼─")

		# down
		elif head == 2:
			pos[0] += 1
			if turn == "R":
				head = 3
				out[pos[0]][pos[1]] = ("┘ " if out[pos[0]][pos[1]] == "  " else "┼─")

			elif turn == "L":
				head = 1
				out[pos[0]][pos[1]] = ("└─" if out[pos[0]][pos[1]] == "  " else "┼─")

		# left
		elif head == 3:
			pos[1] -= 1
			if turn == "R":
				head = 0
				out[pos[0]][pos[1]] = ("└─" if out[pos[0]][pos[1]] == "  " else "┼─")

			if turn == "L":
				head = 2
				out[pos[0]][pos[1]] = ("┌─" if out[pos[0]][pos[1]] == "  " else "┼─")

	# out and remove empty rows
	return "\n".join("".join(row) for row in cleanup(out))

if __name__ == '__main__':
	print(dragon_curve_string(7))
