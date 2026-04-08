"""Week 1 mini-project: build a small reusable math toolbox.

Run:
    python3 weeks/week01/project/math_toolbox.py
"""


def square(x):
    return x * x


def cube(x):
    return x * x * x


def average(a, b, c):
    return (a + b + c) / 3


def is_even(n):
    return n % 2 == 0


def area_rectangle(width, height):
    return width * height


def area_triangle(base, height):
    return 0.5 * base * height


def distance(speed, time):
    return speed * time


def celsius_to_fahrenheit(c):
    return (9 / 5) * c + 32


def factor_count(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1): ## add int to convert the result of n ** 0.5 to an integer, which is necessary because the range function requires integer arguments. This optimization reduces the number of iterations needed to check for factors, improving the efficiency of the is_prime function.
        if n % i == 0:
            return False
    return True

def perimeter_rectangle(width, height): 
    return 2 * (width + height)

def gcd1(a, b):
    while b: ## This loop continues as long as b is not zero. Inside the loop, it updates a to be b and b to be the remainder of a divided by b (a % b). This process effectively reduces the problem size in each iteration, eventually leading to the greatest common divisor when b becomes zero.
        a, b = b, a % b ## Updates a and b for the next iteration. a takes the value of b, and b takes the value of a % b, which is the remainder when a is divided by b.
    return a

def gcd2(a, b):
    while b: 
        a, b = b, a - b
    return a

def main():
    print("Week 1 Math Toolbox")
    print("-------------------")
    print("square(5) =", square(5))
    print("cube(3) =", cube(3))
    print("average(4, 7, 10) =", average(4, 7, 10))
    print("is_even(8) =", is_even(8))
    print("area_rectangle(6, 4) =", area_rectangle(6, 4))
    print("area_triangle(10, 3) =", area_triangle(10, 3))
    print("distance(12, 5) =", distance(12, 5))
    print("celsius_to_fahrenheit(20) =", celsius_to_fahrenheit(20))
    print("factor_count(12) =", factor_count(12))
    print("is_prime(13) =", is_prime(13))
    print("perimeter_rectangle(6, 4) =", perimeter_rectangle(6, 4))
    print("gcd1(500, 300) =", gcd1(500, 300))
    print("gcd2(500, 300) =", gcd2(500, 300))
    print()
    print("Your challenge:")
    print("1. Add a perimeter_rectangle function.")
    print("2. Add a gcd-style function for two numbers later.")
    print("3. Improve is_prime so it checks fewer numbers.")


if __name__ == "__main__":
    main()
