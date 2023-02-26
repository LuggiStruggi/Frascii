from frascii.fractals.mandelbrot import mandelbrot_string
from frascii.fractals.julia import julia_string
from frascii.fractals.sierpinski_carpet import sierpinski_carpet_string
from frascii.fractals.hilbert_curve import hilbert_curve_string
from frascii.fractals.fibonacci import fibonacci_string

__version__ = '1.4'

def mandelbrot(x, y, x_radius, y_radius, stepsize, max_iter):
	return mandelbrot_string(x, y, x_radius, y_radius, stepsize, max_iter)

def julia(f, x, y, x_radius, y_radius, stepsize, max_iter):
	return julia_string(f, x, y, x_radius, y_radius, stepsize, max_iter)

def sierpinski_carpet(n):
	return sierpinski_carpet_string(n)

def hilbert_curve(n):
	return hilbert_curve_string(n)

def fibonacci(n):
	return fibonacci_string(n)
