def sum_of_digits(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    return sum(int(digit) for digit in str(abs(n)))
num = int(input("Enter an integer: "))
print(sum_of_digits(num))