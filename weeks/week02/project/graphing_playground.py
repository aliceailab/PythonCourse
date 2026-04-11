"""Week 2 mini-project: a simple graphing playground.

Run:
    python3 weeks/week02/project/graphing_playground.py
"""

import math


def line(x):
    return 2 * x + 1


def parabola(x):
    return x * x


def shifted_parabola(x):
    return (x - 2) * (x - 2) + 1


def build_points(func, x_values):
    y_values = []
    for x in x_values:
        y_values.append(func(x))
    return y_values


def build_circle(radius, steps):
    x_values = []
    y_values = []
    for i in range(steps + 1):
        theta = 2 * math.pi * i / steps
        x_values.append(radius * math.cos(theta))
        y_values.append(radius * math.sin(theta))
    return x_values, y_values


def main():
    x_values = list(range(-5, 6))

    print("Week 2 Graphing Playground")
    print("-------------------------")
    print("x values:", x_values)
    print("line(x):", build_points(line, x_values))
    print("parabola(x):", build_points(parabola, x_values))
    print("shifted_parabola(x):", build_points(shifted_parabola, x_values))

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print()
        print("matplotlib is not installed yet.")
        print("Install it with: python3 -m pip install matplotlib")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, build_points(line, x_values), marker="o", label="y = 2x + 1")
    plt.plot(x_values, build_points(parabola, x_values), marker="o", label="y = x^2")
    plt.plot(
        x_values,
        build_points(shifted_parabola, x_values),
        marker="o",
        label="y = (x - 2)^2 + 1",
    )

    circle_x, circle_y = build_circle(4, 120)
    plt.plot(circle_x, circle_y, label="circle radius 4")

    plt.axhline(0, color="gray", linewidth=1)
    plt.axvline(0, color="gray", linewidth=1)
    plt.title("Week 2 Graphing Playground")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
