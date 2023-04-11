def l_system(start, rules, n):
	letters = start
	rules = rules.replace("(", "").replace(")", "").replace(" ", "").split(",")
	rules = dict(rule.split("->") for rule in rules)
	for i in range(n):
		letters = "".join(rules[l] if l in rules else l for l in letters)
	return "".join(l for l in letters if l in "+-Ff")
	

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
	out = [["URDL"]]
	pos = [0, 0]  #y, x
	comp = "URDL"
	if start_dir not in "URDL":
		raise ValueError(f"start_dir must be U,R,D or L but was {start_dir}")
	while comp[0] != start_dir:
		comp = comp[1:] + comp[0]
	prev_comp = comp
	buff = ""
	
	for i, turn in enumerate(letters):
		
		# Enlarge grid
		if pos[0] == len(out) - 1:
			out.append(["URDL" for i in range(len(out[0]))])
		if pos[1] == len(out[0]) - 1:
			out = [row + ["URDL"] for row in out]
		if pos[0] == 0:
			out.insert(0, ["URDL" for i in range(len(out[0]))])
			pos[0] = 1
		if pos[1] == 0:
			out = [["URDL"] + row for row in out]
			pos[1] = 1	

		curr = out[pos[0]][pos[1]]
		if turn == "-":
			comp = comp[1:] + comp[0]

		elif turn == "+":
			comp = comp[-1] + comp[:-1]

		elif turn in "fF":
			if turn == "F":
				out[pos[0]][pos[1]] = curr.replace(comp[0], "")
			prev_comp = comp	
			if comp[0] == "U":
				pos[0] -= 1
			elif comp[0] == "R":
				pos[1] += 1
			elif comp[0] == "D":
				pos[0] += 1
			elif comp[0] == "L":
				pos[1] -= 1
			if turn == "F":
				out[pos[0]][pos[1]] = out[pos[0]][pos[1]].replace(comp[2], "")

	# Enlarge grid
	if pos[0] == len(out) - 1:
		out.append(["URDL" for i in range(len(out[0]))])
	if pos[1] == len(out[0]) - 1:
		out = [row + ["URDL"] for row in out]
	if pos[0] == 0:
		out.insert(0, ["URDL" for i in range(len(out[0]))])
		pos[0] = 1
	if pos[1] == 0:
		out = [["URDL"] + row for row in out]
		pos[1] = 1	

	trans = {"URDL": "  ", "URD": "╴ ", "URL": "╷ ", "UDL": "╶─",
			 "RDL": "╵ ", "RL": "│ ", "UD": "──", "UR": "┐ ",
			 "UL": "┌─", "RD": "┘ ", "DL": "└─", "U": "┬─",
			 "R": "┤ ", "D": "┴─", "L": "├─", "": "┼─"}
	return "\n".join("".join(trans[c] for c in row) for row in cleanup(out))


if __name__ == '__main__':
	print(l_system_string("A", "(A->+Bf-AFA-FB+), (B->-AF+BFB+FA-)", 3, "R"))
