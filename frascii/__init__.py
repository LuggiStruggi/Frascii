from frascii.fractals.mandelbrot import mandelbrot_string
from frascii.fractals.julia import julia_string
from frascii.fractals.sierpinski_carpet import sierpinski_carpet_string
from frascii.fractals.sierpinski_triangle import sierpinski_triangle_string
from frascii.fractals.cantor import cantor_string
from frascii.fractals.koch import koch_string
from frascii.fractals.vicsek import vicsek_string
from frascii.fractals.hilbert_curve import hilbert_curve_string
from frascii.fractals.peano_curve import peano_curve_string
from frascii.fractals.dragon_curve import dragon_curve_string
from frascii.fractals.fibonacci import fibonacci_string
from frascii.fractals.l_system import l_system_string

__version__ = '2.2'

def mandelbrot(x, y, x_radius, y_radius, stepsize, max_iter):
	return mandelbrot_string(x, y, x_radius, y_radius, stepsize, max_iter)

def julia(f, x, y, x_radius, y_radius, stepsize, max_iter):
	return julia_string(f, x, y, x_radius, y_radius, stepsize, max_iter)

def sierpinski_carpet(n):
	return sierpinski_carpet_string(n)

def cantor(n):
	return cantor_string(n)

def vicsek(n):
	return vicsek_string(n)

def koch(n):
	return koch_string(n)

def sierpinski_triangle(n):
	return sierpinski_triangle_string(n)

def hilbert_curve(n):
	return hilbert_curve_string(n)

def peano_curve(n):
	return peano_curve_string(n)

def dragon_curve(n):
	return dragon_curve_string(n)

def fibonacci(n):
	return fibonacci_string(n)

def l_system(start, rules, n, direction):
	return l_system_string(start, rules, n, direction)
