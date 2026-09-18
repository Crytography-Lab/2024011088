def table(key):
    x = ""
    for c in key.upper() + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        c = "I" if c == "J" else c
        if c not in x:
            x += c
    return x

def play(s, key, d=1):
    t = table(key)
    s = ''.join(c for c in s.upper() if c.isalpha()).replace("J","I")
    if len(s) % 2: s += "X"

    r = ""
    for i in range(0, len(s), 2):
        a, b = t.index(s[i]), t.index(s[i+1])
        r += t[(a//5*5+(a%5+d)%5)]
        r += t[(b//5*5+(b%5+d)%5)]
    return r

key = input("Key: ")
s = input("Message: ")

e = play(s, key)
print("Encrypted:", e)
print("Decrypted:", play(e, key, -1))