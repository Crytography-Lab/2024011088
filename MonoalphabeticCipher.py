a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = input("Enter 26-letter key: ").upper()

def enc(s):
    return ''.join(key[a.index(c)] if c in a else c for c in s.upper())

def dec(s):
    return ''.join(a[key.index(c)] if c in key else c for c in s)

s = input("Message: ")
e = enc(s)

print("Encrypted:", e)
print("Decrypted:", dec(e))