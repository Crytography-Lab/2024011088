def encrypt(s, n):
    r = [""] * n
    for i, c in enumerate(s):
        r[i % n] += c
    return ''.join(r)

def decrypt(s, n):
    return s  # use standard Rail Fence implementation if required

s = input("Message: ")
n = int(input("Key: "))
print("Encrypted:", encrypt(s, n))