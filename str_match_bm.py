def bmBc(pat:str):

    len_pat = len(pat)
    if not len_pat:
        return [0] * 256
    len_to_right = [len_pat] * 256

    for i in range(len_pat - 1):
            len_to_right[ord(pat[i])] = len_pat - 1 - i

    return len_to_right

def bmGs(pat:str):
    m = len(pat)
    arr_len = [m] * m
    arr_suf = suffix(pat)

    j = 0
    for i in range(m - 1, -1, -1):
        if arr_suf[i] == i + 1:
            while j <= m - 1 - arr_suf[i]:
                arr_len[j] = m - 1 - i
                j = j + 1


    for k in range(m):
        arr_len[m - 1 - arr_suf[k]] = m - 1 - k


    return arr_len


def suffix(pat:str):
    m = len(pat)
    arr_suf = [m] * m
    for i in range(m - 2, -1, -1):
        j = i
        k = m - 1
        while j >= 0 and pat[j] == pat[k]:
            j = j - 1
            k = k - 1
        arr_suf[i] = i - j

    return arr_suf


def bm(text:str, pat:str):

    n = len(text)
    if not n:
        return -1
    m = len(pat)
    if not m:
        return 0
    arr_bc = bmBc(pat)
    arr_gs = bmGs(pat)

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pat[j]:
            j = j - 1
        if j == -1:
            return i
        else:
            tmp = text[i + j]
            tmp2 = ord(text[i + j])
            c = arr_bc[ord(text[i + j])] - m + 1 + j
            i += max(arr_gs[j], arr_bc[ord(text[i + j])] - m + 1 + j)

    return -1



t1 = "hello"
p1 = "ll"

res1 = bm(t1, p1)

t2 = "aaaaa"
p2 = "bba"

res2 = bm(t2, p2)

t3 = "mississippi"
p3 = "issi"
res3 = bm(t3, p3)

print(res1)
print(res2)
print(res3)


