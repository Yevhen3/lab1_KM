import numpy as np

# Функція під інтегралом
def f(x):
    return 1 / np.sqrt(x * (1 + x**2))

# Метод правих прямокутників
def right_rectangle_rule(a, b, n):
    h = (b - a) / n
    integral_approx = 0
    for i in range(1, n + 1):
        integral_approx += f(a + i * h)
    integral_approx *= h
    return integral_approx

# Правило Рунге для оцінки похибки
def runge_rule(I_n, I_2n):
    return  abs(I_2n - I_n)

# Параметри інтегрування
a = 0  # Нижня межа інтегралу
b = 1  # Верхня межа інтегралу
epsilon = 0.5

# Обчислення інтегралу з 4 підінтервалами
n = 4
I_n = right_rectangle_rule(a, b, n)

# Обчислення інтегралу з 8 підінтервалами
n_2 = 8
I_2n = right_rectangle_rule(a, b, n_2)

# Оцінка похибки за правилом Рунге
E = runge_rule(I_n, I_2n)

# Виведення результатів
print(f"Наближене значення інтегралу з {n} підінтервалами: {I_n}")
print(f"Наближене значення інтегралу з {n_2} підінтервалами: {I_2n}")
print(f"Оцінка похибки за правилом Рунге: {E}")


if E <= epsilon:
    print(f"Похибка {E} менша або дорівнює заданій точності {epsilon}.")
else:
    print(f"Похибка {E} більша за задану точність {epsilon}. Потрібно збільшити кількість підінтервалів.")

