import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def newton_fractal(func, func_prime, xlim, ylim, width, height, max_iter):
    # Создание сетки комплексных чисел
    x = np.linspace(xlim[0], xlim[1], width)
    y = np.linspace(ylim[0], ylim[1], height)
    z = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)
    z = z[:, 0] + 1j * z[:, 1]

    img = np.zeros(z.shape, dtype=int)  # Массив для хранения количества итераций

    for i in range(max_iter):
        mask = np.abs(z) < 10  # Условие для продолжения итераций
        z[mask] -= func(z[mask]) / func_prime(z[mask])  # Метод Ньютона
        img[mask] = i  # Сохраняем количество итераций

    return img.reshape(height, width)

def func(z):
    return z ** 4 - 1

def func_prime(z):
    return 4 * z ** 3

xlim = (-2, 2)
ylim = (-2, 2)
width, height = 800, 800
max_iter = 30

# Генерация и отображение бассейна Ньютона
img = newton_fractal(func, func_prime, xlim, ylim, width, height, max_iter)

custom_cmap = ListedColormap(['#c1b8fc', '#fcb8ee', '#cce5fc'])

def plot_newton_fractal(img, xlim, ylim, cmap):
    plt.figure(figsize=(10, 10))
    plt.imshow(img, extent=(xlim[0], xlim[1], ylim[0], ylim[1]), cmap=cmap, interpolation='none')
    plt.show()

plot_newton_fractal(img, xlim, ylim, custom_cmap)
