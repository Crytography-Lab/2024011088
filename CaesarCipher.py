def caesar(s, k):
    r = ""
    for c in s:
        if c.isalpha():
            r += chr((ord(c.upper()) - 65 + k) % 26 + 65)
        else:
            r += c
    return r

s = input("Message: ")
k = int(input("Key: "))

e = caesar(s, k)
print("Encrypted:", e)
print("Decrypted:", caesar(e, -k))