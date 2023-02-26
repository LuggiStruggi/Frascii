# Frascii
Visualizations of Fractals for the Ubuntu (or other) Terminal

Install using `pip install frascii`

# Commands

`frascii sierpinski_carpet <n>`: Displays the n-th iteration of a sierpinski carpet.

`frascii hilbert_curve <n>`: Displays the n-th iteration of a hilbert curve.

`frascii fibonacci <n>`: Displays the fibonacci numbers up to the n-th fibonacci number as squares.

`frascii mandelbrot <x, y, x_radius, y_radius, stepsize, max_iter>`: Displays a specified part of the mandelbrot set.

`frascii julia <f, x, y, x_radius, y_radius, stepsize, max_iter>`: Displays a specified part of the julia set for f(z).


more to come ...

# Examples

## Screenshots of Terminal (zoomed out)
### Mandelbrot set
![Mandelbrot set in terminal by frascii](readme_images/mandelbrot.png)
### Julia set
![Julia set in terminal by frascii](readme_images/julia.png)


## Smaller ASCII Mandelbrot set
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
# Tip for better visualizstion

Make a new custom terminal profile and set its fontsize to 1. (Menu->Preferences->Profiles)
Then you can switch between the default profile and the new one to have "more pixels"

![Preferences](readme_images/profile.png)

![Font](readme_images/fontsize.png)
