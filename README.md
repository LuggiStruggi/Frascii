# Frascii
ASCII-visualizations of Fractals for the Ubuntu (or other) Terminal

Install using `pip install frascii`

# Commands

`frascii sierpinski_carpet <n>`: Displays the n-th iteration of the [Sierpinski Carpet](https://en.wikipedia.org/wiki/Sierpinski_carpet).

`frascii sierpinski_triangle <n>`: Displays the n-th iteration of the [Sierpinski Triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle).

`frascii koch <n>`: Displays the n-th iteration of the [Koch Snowflake](https://en.wikipedia.org/wiki/Koch_snowflake).

`frascii vicsek <n>`: Displays the n-th iteration of the [Vicsek Fractal](https://en.wikipedia.org/wiki/Vicsek_fractal).

`frascii hilbert_curve <n>`: Displays the n-th iteration of the [Hilbert Curve](https://en.wikipedia.org/wiki/Hilbert_curve).

`frascii peano_curve <n>`: Displays the n-th iteration of the [Peano Curve](https://en.wikipedia.org/wiki/Peano_curve).

`frascii dragon_curve <n>`: Displays the n-th iteration of the [Dragon Curve](https://en.wikipedia.org/wiki/Dragon_curve).

`frascii fibonacci <n>`: Displays the [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence) up to n as squares.

`frascii mandelbrot <x, y, x_radius, y_radius, stepsize, max_iter>`: Displays a specified part of the [Mandelbrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set).

`frascii julia <f, x, y, x_radius, y_radius, stepsize, max_iter>`: Displays a specified part of the [Julia Set](https://en.wikipedia.org/wiki/Julia_set) for a given f(z).


more to come ...

# Examples

## Mandelbrot set
`frascii mandelbrot -x_radius 400 -y_radius 180 -stepsize 0.0033`

![Mandelbrot set in terminal by frascii](readme_images/mandelbrot.png)

`frascii mandelbrot -x -1.15 -y 0.26 -x_radius 200 -y_radius 70 -stepsize 3.7e-4 -max_iter 60`

![Mandelbrot set in terminal by frascii](readme_images/mandelbrot2.png)

`frascii mandelbrot`

```
                                                       
                                       ▓░              
                                      ░░▒░▒█           
                                     ░░░██▒░░          
                                  ░░░░▒████▓░░         
                              ░░░░░░░░▒████▒░░░░░░▓    
                            ░░░▒██▓███████████▓▒▒▒▓▒   
                          ░░░░▒▒██████████████████▓░░  
                 ░▒░░░░░░░░░░▒▓███████████████████▓░▓  
                ░░░▓▓▒▒█▒▒░░▒██████████████████████▒░░ 
               ░░░▒▓███████▒▓███████████████████████░  
         ░░░░░░▒▒▒█████████████████████████████████░░  
    █████████████████████████████████████████████▒░░░  
         ░░░░░░▒▒▒█████████████████████████████████░░  
               ░░░▒▓███████▒▓███████████████████████░  
                ░░░▓▓▒▒█▒▒░░▒██████████████████████▒░░ 
                 ░▒░░░░░░░░░░▒▓███████████████████▓░▓  
                          ░░░░▒▒██████████████████▓░░  
                            ░░░▒██▓███████████▓▒▒▒▓▒   
                              ░░░░░░░░▒████▒░░░░░░▓    
                                  ░░░░▒████▓░░         
                                     ░░░██▒░░          
                                      ░░▒░▒█           
                                       ▓░              
```

## Julia set
`frascii julia -f "z**2 - 0.4 + 0.6j" -x_radius 450 -y_radius 180 -stepsize 0.0033`

![Julia set in terminal by frascii](readme_images/julia.png)

`frascii julia -f "z**2 - 0.8" -x_radius 500 -y_radius 150 -stepsize 0.0033 -max_iter 20`

![Julia set in terminal by frascii](readme_images/julia2.png)

`frascii julia -f "2-z**2" -max_iter 5 -stepsize 0.008 -x 1 -x_radius 375 -y_radius 25`

![Julia set in terminal by frascii](readme_images/julia3.png)

## Hilbert Curve

`frascii hilbert_curve -n 4`

![Hilbert curve in terminal by frascii](readme_images/hilbert.png)

`frascii hilbert_curve -n 3`

```
┌─┐ ┌─┐ ┌─┐ ┌─┐
│ └─┘ │ │ └─┘ │
└─┐ ┌─┘ └─┐ ┌─┘
┌─┘ └─────┘ └─┐
│ ┌───┐ ┌───┐ │
└─┘ ┌─┘ └─┐ └─┘
┌─┐ └─┐ ┌─┘ ┌─┐
│ └───┘ └───┘ │

```

## Dragon Curve

`frascii dragon_curve -n 9`

```
                    ┌─┐     ┌─┐                                 
                    └─┼─┐   └─┼─┐                               
                ┌─┐ ┌─┼─┼─┐ ┌─┼─┘                               
                └─┼─┼─┼─┼─┼─┼─┼─┐                   ┌─┐ ┌─┐     
                ┌─┼─┘ └─┼─┼─┼─┼─┘   ┌─┐           ┌─┘ └─┼─┘     
                └─┼─┐   └─┼─┼─┼─┐   └─┼─┐         └─    └─┐ ┌─┐ 
                  └─┘   ┌─┼─┼─┼─┼─┐ ┌─┼─┘               ┌─┼─┼─┘ 
                        └─┼─┼─┼─┼─┼─┼─┼─┐               └─┼─┘   
    ┌─┐     ┌─┐     ┌─┐ ┌─┼─┼─┼─┼─┼─┼─┼─┘   ┌─┐     ┌─┐ ┌─┘     
    └─┼─┐   └─┼─┐   └─┼─┼─┼─┼─┼─┼─┼─┼─┼─┐   └─┼─┐   └─┼─┼─┐ ┌─┐ 
┌─┐ ┌─┼─┼─┐ ┌─┼─┼─┐ ┌─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┐ ┌─┼─┼─┐ ┌─┼─┼─┼─┼─┘ 
└─┼─┼─┼─┼─┼─┼─┼─┼─┼─┘ └─┘ └─┼─┼─┼─┼─┘ └─┘ └─┼─┼─┼─┼─┘ └─┘ └─┘   
┌─┼─┘ └─┼─┼─┼─┼─┼─┘       ┌─┼─┼─┼─┘       ┌─┼─┼─┼─┘             
└─┼─┐   └─┼─┼─┼─┼─┐ ┌─┐   └─┘ └─┼─┐ ┌─┐   └─┘ └─┼─┐ ┌─┐         
  └─┘   ┌─┼─┼─┼─┼─┼─┼─┘       ┌─┼─┼─┼─┘       ┌─┼─┼─┼─┘         
        └─┼─┘ └─┘ └─┘         └─┘ └─┘         └─┘ └─┘           
    ┌─┐ ┌─┘                                                     
    └─┼─┼─┐ ┌─┐                                                 
┌─┐ ┌─┼─┼─┼─┼─┘                                                 
└─┼─┼─┼─┼─┼─┘                                                   
┌─┼─┘ └─┼─┘         ┌─┐                                         
└─┼─┐   └─┐ ┌─┐     ╵ └─┐                                       
  └─┘   ┌─┼─┼─┘       ┌─┘                                       
        └─┼─┼─┐ ┌─┐ ┌─┼─┐                                       
        ┌─┼─┘ └─┼─┼─┘ └─┘                                       
        └─┼─┐   └─┼─┐                                           
          └─┘     └─┘                                           

```
# Tip for better visualization

Make a new custom terminal profile and set its fontsize to 1 (Menu->Preferences->Profiles).
Then you can switch between the default profile and the new one to have "more pixels" on one page.

<img src="readme_images/profile.png" width=25% height=25%>
<img src="readme_images/fontsize.png" width=50% height=50%>
