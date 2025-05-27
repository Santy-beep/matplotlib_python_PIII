# Matplotlib [Python]
# Ejercicios de práctica

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def line_plot():
    # Generaremos la función y=X^2 (x al cuadrado)
    x = range(-10, 11, 1)
    y = []
    for i in x:
        y.append(i**2)

    fig = plt.figure()
    fig.suptitle('Grafico Ejemplo 1 Y=X**2', fontsize=12)
    ax = fig.add_subplot()

    ax.plot(x, y, c='white', marker='*', label='función:y=x**2')
    ax.legend()
    ax.grid()
    ax.set_facecolor('black')
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot")

    x = list(range(-10, 11, 1))

    y = []
    for i in x:
        y.append(i**2)

    line_plot()

    print("terminamos")
