def compress_string(s: str) -> str:
    n = len(s)
    if n == 0:
        return s
    compressed = []
    count = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < n else s
s = input("Enter the string: ")
print("Compressed string:", compress_string(s))