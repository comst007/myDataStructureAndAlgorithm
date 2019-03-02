PRIME = 72057594037927931
DOMAIN = 128

def updateKey(oldVal:int, outVal:int, outWeight,inVal:int):
    val1 = (oldVal - outVal * outWeight + PRIME * DOMAIN) % PRIME
    val2 = val1 * DOMAIN % PRIME
    res = (val2 + inVal) % PRIME
    return res

def karpRabin(text:str, pat:str):
    n = len(text)
    if not n:
        return -1
    m = len(pat)
    if not m:
        return 0
    if m > n:
        return -1
    weight0 = pow(DOMAIN, m - 1) % PRIME
    i = 0
    hash_t = 0
    hash_p = 0
    while i < m:
        hash_t = (hash_t * DOMAIN + ord(text[i])) % PRIME
        hash_p = (hash_p * DOMAIN + ord(pat[i])) % PRIME
        i += 1

    i = 0
    while i <= n - m:
        if hash_t == hash_p:
            k = 0
            while k < m and text[i + k] == pat[k]:
                k += 1
            if k < m:
                i += 1
            else:
                return i

        else:
            if i == n - m:
                return -1
            else:
                hash_t = updateKey(hash_t, ord(text[i]), weight0, ord(text[i + m]))
                i += 1

    return -1


p = 1 << 56 - 1

t1 = "missipissipl"
p = "issi"
res = karpRabin(t1, p)
print(res)