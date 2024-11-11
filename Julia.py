import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as clr

def julia_set(c, xlim, ylim, width, height, max_iter):
    # Создаем двумерную сетку комплексных чисел
    x = np.linspace(xlim[0], xlim[1], width)
    y = np.linspace(ylim[0], ylim[1], height)
    z = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)
    z = z[:, 0] + 1j * z[:, 1]

    # Инициализируем массив для хранения количества итераций
    img = np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(z) < 2  # Фильтр для значений, остающихся в пределах радиуса 2
        img[mask] = i
        z[mask] = z[mask] ** 2 + c  # Итерация для каждого значения

    return img.reshape(height, width)

c = -0.5251993 + 0.5251993j
xlim = (-2, 2)
ylim = (-2, 2)
width, height = 800, 800
max_iter = 200  # Максимальное количество итераций

# Генерация и отображение множества Жюлиа
img = julia_set(c, xlim, ylim, width, height, max_iter)
colorpoints = [(1 - (1 - q) ** 4, c) for q, c in zip(np.linspace(0, 1, 20),
                                                     cycle(['#cce5fc', '#c1b8fc', '#fcb8ee' ]))] #голубой, розовый, сиреневый
cmap = clr.LinearSegmentedColormap.from_list('mycmap',
                                             colorpoints, N=2048)
plt.figure(figsize=(10, 10))
plt.imshow(img, cmap=cmap, interpolation='none')
plt.show()
