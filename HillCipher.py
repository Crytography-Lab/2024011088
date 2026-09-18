def hill(s, k):
    s = ''.join(c for c in s.upper() if c.isalpha())
    if len(s) % 2: s += "X"
    r = ""

    for i in range(0, len(s), 2):
        a, b = ord(s[i])-65, ord(s[i+1])-65
        r += chr((k[0][0]*a+k[0][1]*b)%26+65)
        r += chr((k[1][0]*a+k[1][1]*b)%26+65)

    return r

key = [[3,3],[2,5]]
s = input("Message: ")

e = hill(s, key)
print("Encrypted:", e)

# Inverse of [[3,3],[2,5]] mod 26
inv = [[15,17],[20,9]]
print("Decrypted:", hill(e, inv))