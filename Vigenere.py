def vig(s, key, d=1):
    r = ""
    for i, c in enumerate(s.upper()):
        if c.isalpha():
            x = ord(key[i % len(key)].upper()) - 65
            r += chr((ord(c) - 65 + d*x) % 26 + 65)
    return r

s = input("Message: ")
key = input("Key: ")

e = vig(s, key)
print("Encrypted:", e)
print("Decrypted:", vig(e, key, -1))