def catx(arr1, arr2):
    return [r1 + r2 for r1, r2 in zip(arr1, arr2)]

def caty(arr1, arr2):
    return arr1 + arr2

def reducer(arr):
    return [r[:-1] for r in arr]

def reducel(arr):
    return [r[1:] for r in arr]

def reducet(arr):
    return arr[1:]

def reduceb(arr):
    return arr[:-1]

def square(n):
    top = [["┌"] + ["─"]*(2*n+1) + ["┐"]]
    mid = [["│"] + [" "]*(2*n+1) + ["│"]]*n
    bot = [["└"] + ["─"]*(2*n+1) + ["┘"]]
    return top + mid + bot

def fibonacci(n):
    if n == 0:
        return square(0)
    f = fibonacci(n-1)
    if n % 4 == 3:
        l = len(f)-2
        f[0][0] = "┬"
        f[-1][0] = "┴"
        return catx(reducer(square(l)), f)
    elif n % 4 == 0:
        f[-1][0] = "├"
        f[-1][-1] = "┤"
        w = len(f[0])//2 - 1
        return caty(f, reducet(square(w)))
    elif n % 4 == 1:
        l = len(f)-2
        f[0][-1] = "┬"
        f[-1][-1] = "┴"
        return catx(f, reducel(square(l)))
    elif n % 4 == 2:
        f[0][0] = "├"
        f[0][-1] = "┤"
        w = len(f[0])//2 - 1
        return caty(reduceb(square(w)), f)

def fibonacci_string(n):
    return "\n".join("".join(row) for row in fibonacci(n))

if __name__ == '__main__':
	print(fibonacci_string(3))
