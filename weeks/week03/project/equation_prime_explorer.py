"""Week 3 mini-project: algebra and number theory explorer.

Run:
    python3 weeks/week03/project/equation_prime_explorer.py
"""


def is_divisible(a, b):
    return a % b == 0


def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_up_to(n):
    result = []
    for value in range(2, n + 1):
        if is_prime(value):
            result.append(value)
    return result


def solve_linear_by_search(target, x_values):
    solutions = []
    for x in x_values:
        if 2 * x + 3 == target:
            solutions.append(x)
    return solutions


def solve_quadratic_by_search(x_values):
    solutions = []
    for x in x_values:
        if x * x - 5 * x + 6 == 0:
            solutions.append(x)
    return solutions


def main():
    print("Week 3 Equation and Prime Explorer")
    print("----------------------------------")
    print("is_divisible(12, 3) =", is_divisible(12, 3))
    print("factors(18) =", factors(18))
    print("gcd(12, 18) =", gcd(12, 18))
    print("lcm(12, 18) =", lcm(12, 18))
    print("is_prime(13) =", is_prime(13))
    print("primes_up_to(30) =", primes_up_to(30))
    print("solve 2x + 3 = 11 over -10..10:", solve_linear_by_search(11, range(-10, 11)))
    print("solve x^2 - 5x + 6 = 0 over -10..10:", solve_quadratic_by_search(range(-10, 11)))

    try:
        import sympy as sp
    except ImportError:
        print()
        print("sympy is not installed yet.")
        print("Install it with: python3 -m pip install --user sympy")
        return

    x = sp.symbols("x")
    print()
    print("Sympy section")
    print("solve(2*x + 3 - 11) =", sp.solve(sp.Eq(2 * x + 3, 11), x))
    print("solve(x^2 - 5*x + 6) =", sp.solve(sp.Eq(x ** 2 - 5 * x + 6, 0), x))
    print("factor(x^2 - 5*x + 6) =", sp.factor(x ** 2 - 5 * x + 6))


if __name__ == "__main__":
    main()
