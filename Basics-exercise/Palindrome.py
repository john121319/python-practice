#Palindrome checker
def is_palindrom(c):
  return c == c[::-1]

s = input('enter a string ')

if is_palindrom(s):
  print(f"'{s}' is a palindrom.")
else:
  print(f"'{s}' is not a palindrom.")
