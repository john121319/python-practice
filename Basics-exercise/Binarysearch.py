def binary_search(a, t):
    if t not in a:
        raise ValueError("Input must be among the list.")
    l, r = 0, len(a) - 1

    while l <= r:
        mid = (l + r) // 2

        if a[mid] == t:
            return mid
        elif a[mid] < t:
            l = mid + 1
        else:
            r = mid - 1

while True:
  try:
    n = [2, 4, 6, 8, 10, 12]
    t = int(input(f"Enter an integer among {n}: "))
    print(f"the index of {t} is: ",binary_search(n, t))
    break
  except ValueError as e:
          print(e)

