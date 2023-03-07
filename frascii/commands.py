import frascii
import argparse

def cmd_main():
	fc = argparse.ArgumentDefaultsHelpFormatter
	parser = argparse.ArgumentParser(prog="frascii", description="ASCII visualization of fractals for the terminal.", formatter_class=fc)
	subparsers = parser.add_subparsers(dest="subcommand")

	# Sierpinski carpet sub-command
	sierpinski_parser = subparsers.add_parser("sierpinski_carpet", description="Wikipedia: https://en.wikipedia.org/wiki/Sierpinski_carpet", formatter_class=fc)
	sierpinski_parser.add_argument("-n", type=int, help="iterations", choices=range(0, 7), nargs="?", default=2)
	sierpinski_parser.set_defaults(func=frascii.sierpinski_carpet)

	# Sierpinski triangle sub-command
	sierpinski_parser = subparsers.add_parser("sierpinski_triangle", description="Wikipedia: https://en.wikipedia.org/wiki/Sierpinski_triangle", formatter_class=fc)
	sierpinski_parser.add_argument("-n", type=int, help="iterations", choices=range(0, 10), nargs="?", default=3)
	sierpinski_parser.set_defaults(func=frascii.sierpinski_triangle)

	# Cantor set sub-command
	cantor_parser = subparsers.add_parser("cantor", description="Wikipedia: https://en.wikipedia.org/wiki/Cantor_set", formatter_class=fc)
	cantor_parser.add_argument("-n", type=int, help="iterations", choices=range(0, 7), nargs="?", default=2)
	cantor_parser.set_defaults(func=frascii.cantor)

	# Koch snowflake sub-command
	koch_parser = subparsers.add_parser("koch", description="Wikipedia: https://en.wikipedia.org/wiki/Koch_snowflake", formatter_class=fc)
	koch_parser.add_argument("-n", type=int, help="iterations", choices=range(0, 7), nargs="?", default=2)
	koch_parser.set_defaults(func=frascii.koch)

	# Vicsek fractal sub-command
	vicsek_parser = subparsers.add_parser("vicsek", description="Wikipedia: https://en.wikipedia.org/wiki/Vicsek_fractal", formatter_class=fc)
	vicsek_parser.add_argument("-n", type=int, help="iterations", choices=range(0, 7), nargs="?", default=2)
	vicsek_parser.set_defaults(func=frascii.vicsek)

	# Hilbert curve sub-command
	hilbert_parser = subparsers.add_parser("hilbert_curve", description="Wikipedia: https://en.wikipedia.org/wiki/Hilbert_curve", formatter_class=fc)
	hilbert_parser.add_argument("-n", type=int, help="iterations", choices=range(1, 10), nargs="?", default=3)
	hilbert_parser.set_defaults(func=frascii.hilbert_curve)

	# Peano curve sub-command
	peano_parser = subparsers.add_parser("peano_curve", description="Wikipedia: https://en.wikipedia.org/wiki/Peano_curve", formatter_class=fc)
	peano_parser.add_argument("-n", type=int, help="iterations", choices=range(1, 7), nargs="?", default=2)
	peano_parser.set_defaults(func=frascii.peano_curve)

	# Dragon curve sub-command
	dragon_parser = subparsers.add_parser("dragon_curve", description="Wikipedia: https://en.wikipedia.org/wiki/Dragon_curve", formatter_class=fc)
	dragon_parser.add_argument("-n", type=int, help="iterations", choices=range(0, 18), nargs="?", default=7)
	dragon_parser.set_defaults(func=frascii.dragon_curve)

	# Fibonacci sub-command
	fibonacci_parser = subparsers.add_parser("fibonacci", description="Wikipedia: https://en.wikipedia.org/wiki/Fibonacci_number", formatter_class=fc)
	fibonacci_parser.add_argument("-n", type=int, help="iterations", choices=range(0, 14), nargs="?", default=3)
	fibonacci_parser.set_defaults(func=frascii.fibonacci)

	# Mandelbrot sub-command
	mandelbrot_parser = subparsers.add_parser("mandelbrot", description="Wikipedia: https://en.wikipedia.org/wiki/Mandelbrot_set", formatter_class=fc)
	mandelbrot_parser.add_argument("-x", type=float, help="real part of the images center", nargs="?", default=-0.8)
	mandelbrot_parser.add_argument("-y", type=float, help="imaginary part of the images center", nargs="?", default=0)
	mandelbrot_parser.add_argument("-x_radius", type=int, help="pixels added on left and right of center", nargs="?", default=27)
	mandelbrot_parser.add_argument("-y_radius", type=int, help="pixels added on top and bottom of center", nargs="?", default=12)
	mandelbrot_parser.add_argument("-stepsize", type=float, help="size of a pixel", nargs="?", default=0.05)
	mandelbrot_parser.add_argument("-max_iter", type=int, help="iterations after which z is assumed to be in the set", nargs="?", default=20)
	mandelbrot_parser.set_defaults(func=frascii.mandelbrot)

	# Julia sub-command
	julia_parser = subparsers.add_parser("julia", description="Wikipedia: https://en.wikipedia.org/wiki/Julia_set", formatter_class=fc)
	julia_parser.add_argument("-f", type=str, help="complex function", nargs="?", default="z**2 - 0.4 + 0.6j")
	julia_parser.add_argument("-x", type=float, help="real part of the images center", nargs="?", default=0)
	julia_parser.add_argument("-y", type=float, help="imaginary part of the images center", nargs="?", default=0)
	julia_parser.add_argument("-x_radius", type=int, help="pixels added on left and right of center", nargs="?", default=45)
	julia_parser.add_argument("-y_radius", type=int, help="pixels added on top and bottom of center", nargs="?", default=18)
	julia_parser.add_argument("-stepsize", type=float, help="size of a pixel", nargs="?", default=0.033)
	julia_parser.add_argument("-max_iter", type=int, help="iterations after which z is assumed to be in the set", nargs="?", default=40)
	julia_parser.set_defaults(func=frascii.julia)

	# L-system sub-command
	l_system_parser = subparsers.add_parser("l_system", description="Wikipedia: https://en.wikipedia.org/wiki/L-system", formatter_class=fc)
	l_system_parser.add_argument("-start", type=str, help="real part of the images center", nargs="?", default="F")
	l_system_parser.add_argument("-rules", type=str, help="imaginary part of the images center", nargs="?", default="(F->F+F-F-F+F)")
	l_system_parser.add_argument("-n", type=int, help="pixels added on left and right of center", nargs="?", default=3)
	l_system_parser.add_argument("-direction", type=str, help="pixels added on top and bottom of center", choices=["U", "R", "D", "L"], nargs="?", default="U")
	l_system_parser.set_defaults(func=frascii.l_system)


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
