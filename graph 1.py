import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x) * np.cos(x**2 + 8)


def kas(x, x0, pr_x0):
    fx0 = f(x0)
    return fx0 + pr_x0 * (x - x0)


def norm(x, x0, pr_x0):
    fx0 = f(x0)
    return fx0 - (1/pr_x0) * (x - x0)


x = np.linspace(0, 5, 1000)
y = f(x)
y_mn = np.min(y)
y_mx = np.max(y)
x_mn = x[np.argmin(y)]
x_mx = x[np.argmax(y)]
f_pr1 = np.gradient(y, x)
f_pr2 = np.gradient(f_pr1, x)

x0 = float(input('x0 = '))
pr_x0 = np.interp(x0, x, f_pr1)
x_kas = np.linspace(x0-1, x0+1, 1000)
y_kas = kas(x_kas, x0, pr_x0)
x_norm = np.linspace(x0-1, x0+1, 1000)
y_norm = norm(x_norm, x0, pr_x0)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1) # y = f(x)
plt.plot(x, y, label="y = f(x)")
plt.plot(x_kas, y_kas, label="kas", color="black")
plt.plot(x_norm, y_norm, label="norm", color="black")
plt.scatter(x0, f(x0), color='black')
plt.scatter(x_mn, y_mn, color='red')
plt.scatter(x_mx, y_mx, color='red')
plt.grid()
plt.title("y = f(x)")

plt.subplot(2, 2, 2) # y = f'(x)
plt.plot(x, f_pr1, label="y = f'(x)")
plt.grid()
plt.title("y = f\'(x)")

plt.subplot(2, 2, 3) # y = f"(x)
plt.plot(x, f_pr2, label="y = f''(x)")
plt.grid()
plt.title("y = f\"(x)")

plt.show()