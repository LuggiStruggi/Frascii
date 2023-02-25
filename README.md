# Frascii
Visualizations of Fractals for the Ubuntu (or other) Terminal

Install using `pip install frascii`

# Commands

`frascii sierpinski_carpet <n>`: Displays the n-th iteration of a sierpinski carpet.

`frascii hilbert_curve <n>`: Displays the n-th iteration of a hilbert curve.

`frascii fibonacci <n>`: Displays the fibonacci numbers up to the n-th fibonacci number as squares.

`frascii mandelbrot <x, y, x_radius, y_radius, stepsize, max_iter>`: Displays a specified part of the mandelbrot set.

more to come ...

# Examples

## Screenshot of Terminal (zoomed out)
![Mandelbrot set in terminal by frascii](readme_images/mandelbrot.png)

## Smaller ASCII Mandelbrot
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
## ASCII Hilbert Curve, n = 3
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
