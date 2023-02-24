import numpy as np

def hilbert_curve(n):
    if n == 1:
        return np.array([[1, 2], [0, 3]])
    h = hilbert_curve(n-1)
    add = 4 ** (n-1)
    h_up = np.concatenate((h+add, h+2*add), axis=1)
    h_down = np.concatenate((np.flipud(np.rot90(h, k=3)), np.flipud(np.rot90(h))+3*add), axis=1)
    h = np.concatenate((h_up, h_down))
    return h

def hilbert_curve_string(iterations):
    arr = hilbert_curve(iterations)
    out = ""
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i != 0 and i != n-1 and abs(arr[i-1][j] - arr[i][j]) == 1 and abs(arr[i+1][j] - arr[i][j]) == 1:
                out += "│ "
            elif j != 0 and j != n-1 and abs(arr[i][j-1] - arr[i][j]) == 1 and abs(arr[i][j+1] - arr[i][j]) == 1:
                out += "──"
            elif j != 0 and i != n-1 and abs(arr[i][j-1] - arr[i][j]) == 1 and abs(arr[i+1][j] - arr[i][j]) == 1:
                out += "┐ "
            elif j != 0 and i != 0 and abs(arr[i][j-1] - arr[i][j]) == 1 and abs(arr[i-1][j] - arr[i][j]) == 1:
                out += "┘ "
            elif i != 0 and j != n-1 and abs(arr[i-1][j] - arr[i][j]) == 1 and abs(arr[i][j+1] - arr[i][j]) == 1:
                out += "└─"
            elif i != n-1 and j != n-1 and abs(arr[i+1][j] - arr[i][j]) == 1 and abs(arr[i][j+1] - arr[i][j]) == 1:
                out += "┌─"
            else:
                out += "│ " if iterations % 2 else "──"
            if j == n-1:
                out = out[:-1] + "\n"
    return out[:-1]

if __name__ == '__main__':
	print(hilbert_curve_string(3))
