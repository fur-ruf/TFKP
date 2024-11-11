import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as clr

# максимумы для действительной и мнимой частей числа c = p + iq - pmin, pmax, qmin, qmax
# число точек по горизонтали и вертикали - ppoints, qpoints
# максимальное количество итераций - max_iterations
# если ушли на это расстояние, считаем, что ушли на бесконечность - infinity_border

def mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints,
               max_iterations=200, infinity_border=10):
    image = np.zeros((ppoints, qpoints))
    p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax:(qpoints*1j)]
    c = p + 1j*q
    z = np.zeros_like(c)
    for k in range(max_iterations):
        z = z**2 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan
    return -image.T

plt.figure(figsize=(10, 10))
colorpoints = [(1 - (1 - q) ** 4, c) for q, c in zip(np.linspace(0, 1, 20),
                                                     cycle(['#c1b8fc', '#cce5fc', '#fcb8ee']))] #голубой, розовый, сиреневый
cmap = clr.LinearSegmentedColormap.from_list('mycmap',
                                             colorpoints, N=2048)

plt.xticks([])
plt.yticks([])

image = mandelbrot(-2.5, 1.5, 1000, -2, 2, 1000)
plt.imshow(image, cmap=cmap, interpolation='none')

plt.show()

# Если хотим посмотрец поближе:
# p_center, q_center = -0.793191078177363, 0.16093721735804
# for i in range(1,11):
#     scalefactor = i / 12000
#
#     plt.xticks([])
#     plt.yticks([])
#
#     pmin_ = (pmin - p_center) * scalefactor + p_center
#     qmin_ = (qmin - q_center) * scalefactor + q_center
#     pmax_ = (pmax - p_center) * scalefactor + p_center
#     qmax_ = (qmax - q_center) * scalefactor + q_center
#     image = mandelbrot(pmin_, pmax_, 500, qmin_, qmax_, 500)
#     print("(", pmin_, ",", pmax_, ") (", qmin_, ",", qmax_, ")")
#
#     plt.figure(figsize=(10, 10))
#     plt.imshow(image, cmap='flag', interpolation='none')
#     filename = "/Users/amoremore/PycharmProjects/pythonProject2/image/mandelbrot-" + str(i) + ".png"
#     plt.savefig(filename, format="png")
#     print(filename  + " saved")
