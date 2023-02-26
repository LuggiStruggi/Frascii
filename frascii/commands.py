import frascii
import argparse

def cmd_main():
	parser = argparse.ArgumentParser(prog="frascii", description="ASCII visualization of fractals for the terminal.")
	subparsers = parser.add_subparsers(dest="subcommand")

	# Sierpinski carpet sub-command
	sierpinski_parser = subparsers.add_parser("sierpinski_carpet", description="Wikipedia: https://en.wikipedia.org/wiki/Sierpinski_carpet")
	sierpinski_parser.add_argument("n", type=int, help="iterations", choices=range(0, 7), nargs="?", default=2)
	sierpinski_parser.set_defaults(func=frascii.sierpinski_carpet)

	# Hilbert curve sub-command
	hilbert_parser = subparsers.add_parser("hilbert_curve", description="Wikipedia: https://en.wikipedia.org/wiki/Hilbert_curve")
	hilbert_parser.add_argument("n", type=int, help="iterations", choices=range(1, 10), nargs="?", default=3)
	hilbert_parser.set_defaults(func=frascii.hilbert_curve)

	# Fibonacci sub-command
	fibonacci_parser = subparsers.add_parser("fibonacci", description="Wikipedia: https://en.wikipedia.org/wiki/Fibonacci_number")
	fibonacci_parser.add_argument("n", type=int, help="iterations", choices=range(0, 14), nargs="?", default=3)
	fibonacci_parser.set_defaults(func=frascii.fibonacci_string)

	# Mandelbrot sub-command
	mandelbrot_parser = subparsers.add_parser("mandelbrot", description="Wikipedia: https://en.wikipedia.org/wiki/Mandelbrot_set")
	mandelbrot_parser.add_argument("-x", type=float, help="real part of the images center", nargs="?", default=-0.8)
	mandelbrot_parser.add_argument("-y", type=float, help="imaginary part of the images center", nargs="?", default=0)
	mandelbrot_parser.add_argument("-x_radius", type=int, help="pixels added on left and right of center", nargs="?", default=27)
	mandelbrot_parser.add_argument("-y_radius", type=int, help="pixels added on top and bottom of center", nargs="?", default=12)
	mandelbrot_parser.add_argument("-stepsize", type=float, help="size of a pixel", nargs="?", default=0.05)
	mandelbrot_parser.add_argument("-max_iter", type=int, help="iterations after which z is assumed to be in the set", nargs="?", default=20)
	mandelbrot_parser.set_defaults(func=frascii.mandelbrot_string)

	# Mandelbrot sub-command
	julia_parser = subparsers.add_parser("julia", description="Wikipedia: https://en.wikipedia.org/wiki/Julia_set")
	julia_parser.add_argument("-f", type=str, help="complex function", nargs="?", default="z**2 - 0.4 + 0.6j")
	julia_parser.add_argument("-x", type=float, help="real part of the images center", nargs="?", default=0)
	julia_parser.add_argument("-y", type=float, help="imaginary part of the images center", nargs="?", default=0)
	julia_parser.add_argument("-x_radius", type=int, help="pixels added on left and right of center", nargs="?", default=45)
	julia_parser.add_argument("-y_radius", type=int, help="pixels added on top and bottom of center", nargs="?", default=18)
	julia_parser.add_argument("-stepsize", type=float, help="size of a pixel", nargs="?", default=0.033)
	julia_parser.add_argument("-max_iter", type=int, help="iterations after which z is assumed to be in the set", nargs="?", default=40)
	julia_parser.set_defaults(func=frascii.julia_string)

	args = parser.parse_args()
	if args.subcommand == None:
		parser.print_help()
		parser.exit()
		return
	func = args.func
	a = {key: value for key, value in args.__dict__.items() if key not in ['func', 'subcommand']}
	result = func(**a)
	print(result)

if __name__ == '__main__':
	cmd_main()
