import numpy as np
import matplotlib.pyplot as plt


def plot_func(func, x_interval=(0,1), y_interval=(0,1), n_x=50, n_y=30, **plot_args):
    
    X = np.linspace(*x_interval, num=n_x)
    Y = np.linspace(*y_interval, num=n_y)
    X,Y = np.meshgrid(X,Y)
    Z = func(X,Y)
    plt.contour(X,Y,Z, **plot_args)
    
    max_abs = np.amax(np.abs(Z))
    return max_abs


def h(x,y, a=2, b=1, c=3, d=150):
    return d-(c*(x-a)**2+(y-b)**2)

def main():
    N = 20
    x_int = (-20,30)
    y_int = (-15,20)
    f = lambda x,y: h(x,y, 2,2,0.6,150) - h(x,y, 15,2,0.8,200)
    max_f = plot_func(f, x_int, y_int,
                      levels=N, cmap="seismic", alpha=0.5)
    max_g = 1
    clim = max(max_f, max_g)
    plt.clim(-clim, clim ) # set limits of colorbar such that 0 is white, negative is blue, positive is red
    plt.colorbar()
    plt.axis("scaled")
    plt.show()


if __name__=="__main__":
    main()