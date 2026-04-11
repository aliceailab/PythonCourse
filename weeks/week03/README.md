# Week 3: Algebra and Number Theory with Python

This week is about using Python to explore algebra and number theory ideas.

You will practice:

- solving simple equations
- checking divisibility
- finding factors
- working with greatest common divisor and least common multiple
- using modular arithmetic
- generating prime numbers
- trying symbolic math with `sympy`

The goal is to make Python feel like a math lab for patterns, structure, and reasoning.

## What You Will Be Able to Do

By the end of Week 3, you should be able to:

- test whether one number divides another
- compute factors of an integer
- write `gcd` and `lcm` style functions
- check whether a number is prime
- build a list of primes in a range
- solve simple equations with Python and optionally with `sympy`

## How To Study This Week

Use 4 study days. Aim for 60 to 90 minutes each day.

### Day 1: Divisibility and Factors

Learn:

- divisibility
- remainders with `%`
- factors of a number

Practice:

- test whether one number divides another
- list the factors of 12, 18, and 30
- count how many factors a number has

### Day 2: GCD, LCM, and Primes

Learn:

- greatest common divisor
- least common multiple
- prime numbers

Practice:

- write a `gcd` function
- write an `lcm` function
- test whether a number is prime
- generate primes up to 50

### Day 3: Algebra with Python

Learn:

- evaluate expressions
- represent equations as functions
- solve simple equations by checking values
- optional symbolic solving with `sympy`

Practice:

- evaluate `2x + 3`
- solve `2x + 3 = 11`
- solve `x^2 - 5x + 6 = 0`

### Day 4: Mini-Project

Build and test:

- `weeks/week03/project/equation_prime_explorer.py`

Your mini-project should explore:

- factors
- gcd and lcm
- prime testing
- simple equation solving

## Files For This Week

- [Exercises](exercises.md)
- [Guided notebook](notebooks/week03-workout.ipynb)
- [Exercise notebook](notebooks/week03-exercises.ipynb)
- [Mini-project starter](project/equation_prime_explorer.py)

## How To Run Python Files

From the repo root:

```bash
python3 weeks/week03/project/equation_prime_explorer.py
```

## Optional Setup

If you want symbolic solving in the notebook and project, install `sympy`:

```bash
python3 -m pip install --user sympy
```

The week still works even without `sympy`, because the core number theory functions use plain Python first.

## Week 3 Checklist

- I can test divisibility with `%`.
- I can list the factors of an integer.
- I can write a basic `gcd` function.
- I can write a basic `lcm` function.
- I can test whether a number is prime.
- I can solve simple algebra equations by code.
- I can read and edit `equation_prime_explorer.py`.

## After This Week

Once this feels comfortable, Week 4 will focus on:

- geometry
- vectors
- function graphs
- derivatives and area ideas
