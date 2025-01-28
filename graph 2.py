import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, Button


def f(x):
    return np.sin(x) * np.cos(x**2 + 5)


def kas(x, x0, pr_x0):
    f_x0 = f(x0)
    return f_x0 + pr_x0 * (x - x0)


def norm(x, x0, pr_x0):
    f_x0 = f(x0)
    return f_x0 - (1 / pr_x0) * (x - x0)


x = np.linspace(0, 5, 1000)
y = f(x)
f_pr1 = np.gradient(y, x)
f_pr2 = np.gradient(f_pr1, x)

x0 = float(input('x0 = '))
pr_x0 = np.interp(x0, x, f_pr1)
x_kas = np.linspace(x0 - 2, x0 + 2, 1000)
y_kas = kas(x_kas, x0, pr_x0)
x_norm = np.linspace(x0 - 2, x0 + 2, 1000)
y_norm = norm(x_norm, x0, pr_x0)

graph = plt.subplot(1,1,1)
graph.plot(x, y, label='y = f(x)', color='red')
kas_line, = plt.plot(x_kas, y_kas, label='kas', color='black')
norm_line, = plt.plot(x_norm, y_norm, label='norm', color='black')
point_x0, = plt.plot(x0, f(x0), 'o', label='x0', color='black')
plt.grid()


def update_graph():
    global graph, kas_line, norm_line, point_x0, button_colors, slider_x0

    colors = {'красный': 'red', 'зеленый': 'green', 'синий': 'blue'}
    style = colors[button_colors.value_selected]
    graph.plot(x, y, style)

    x0 = slider_x0.val
    pr_x0 = np.interp(x0, x, f_pr1)
    x_kas = np.linspace(x0 - 2, x0 + 2, 1000)
    y_kas = kas(x_kas, x0, pr_x0)
    x_norm = np.linspace(x0 - 2, x0 + 2, 1000)
    y_norm = norm(x_norm, x0, pr_x0)

    norm_line.set_data(x_norm, y_norm)
    kas_line.set_data(x_kas, y_kas)
    point_x0.set_data([x0], [f(x0)])


    plt.draw()


def click_check(label):
    update_graph()


def x0_move(value):
    update_graph()


def button_colors_update(label):
    update_graph()


def reset_slider(value):
    slider_x0.set_val(x0)
    update_graph()


def kas_update(bool):
    global kas_visible
    kas_visible = not kas_visible
    kas_line.set_visible(kas_visible)
    update_graph()


def norm_update(bool):
    global norm_visible
    norm_visible = not norm_visible
    norm_line.set_visible(norm_visible)
    update_graph()


plt.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.55) # Отступ от графика
axes_slider_x0 = plt.axes((0.05, 0.35, 0.85, 0.04))
slider_x0 = Slider(axes_slider_x0, label='x0', valmin=0, valmax=5, valinit=x0, valstep=0.01)
slider_x0.on_changed(x0_move)

axes_reset_button = plt.axes((0.35, 0.15, 0.23, 0.1))
reset_button = Button(axes_reset_button, 'начальное\nположение')
reset_button.on_clicked(reset_slider)

button_axes = plt.axes((0.05, 0.05, 0.2, 0.2))
button_colors = RadioButtons(button_axes, ['красный', 'зеленый', 'синий'])
button_colors.on_clicked(button_colors_update)

kas_visible = True
axes_kas_visible = plt.axes((0.6, 0.15, 0.2, 0.1))
button_kas = Button(axes_kas_visible, 'касательная')
button_kas.on_clicked(kas_update)

norm_visible = True
axes_norm_visible = plt.axes((0.6, 0.05, 0.2, 0.1))
button_norm = Button(axes_norm_visible, 'нормаль')
button_norm.on_clicked(norm_update)


plt.show()