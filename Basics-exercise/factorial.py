def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
while True:
  try:
    n = int(input("Enter an integer: "))
    print(factorial(n))
    break
  except ValueError as e:
          print(e)

