from scipy.integrate import quad
from value_integral import f, a, b
import numpy as np


def monte_carlo_integration(func, lower_limit, upper_limit, num_samples=10000):
    x_samples = np.random.uniform(lower_limit, upper_limit, num_samples)
    y_samples = func(x_samples)
    integral_approximation = np.mean(y_samples) * (upper_limit - lower_limit)
    return integral_approximation


def main():
    exact_integral, _ = quad(f, a, b)

    monte_carlo_result = monte_carlo_integration(f, a, b)

    print(f"Точне значення інтеграла: {exact_integral}")
    print(f"Результат методу Монте-Карло: {monte_carlo_result}")


if __name__ == "__main__":
    main()
