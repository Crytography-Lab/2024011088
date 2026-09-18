def trans(s, key):
    n = len(key)
    while len(s) % n:
        s += "X"

    rows = [s[i:i+n] for i in range(0, len(s), n)]
    order = sorted(range(n), key=lambda i: key[i])

    return ''.join(row[i] for i in order for row in rows)

s = input("Message: ")
k1 = input("Key 1: ")
k2 = input("Key 2: ")

e = trans(trans(s, k1), k2)
print("Encrypted:", e)