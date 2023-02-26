# Frascii
ASCII-visualizations of Fractals for the Ubuntu (or other) Terminal

Install using `pip install frascii`

# Commands

`frascii sierpinski_carpet <n>`: Displays the n-th iteration of a sierpinski carpet.

`frascii hilbert_curve <n>`: Displays the n-th iteration of a hilbert curve.

`frascii fibonacci <n>`: Displays the fibonacci numbers up to the n-th fibonacci number as squares.

`frascii mandelbrot <x, y, x_radius, y_radius, stepsize, max_iter>`: Displays a specified part of the mandelbrot set.

`frascii julia <f, x, y, x_radius, y_radius, stepsize, max_iter>`: Displays a specified part of the julia set for f(z).


more to come ...

# Examples

## Mandelbrot set
`frascii mandelbrot -x_radius 400 -y_radius 180 -stepsize 0.0033`

![Mandelbrot set in terminal by frascii](readme_images/mandelbrot.png)

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

## ASCII Hilbert Curve

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
# Tip for better visualization

Make a new custom terminal profile and set its fontsize to 1 (Menu->Preferences->Profiles).
Then you can switch between the default profile and the new one to have "more pixels" on one page.

<img src="readme_images/profile.png" width=25% height=25%>
<img src="readme_images/fontsize.png" width=50% height=50%>
