def horspool(text:str, pat:str):
    n = len(text)
    if not n:
        return -1
    m = len(pat)
    if not m:
        return 0
    arr_bc = [m] * 256

    for x in range(m - 1):
        arr_bc[ord(pat[x])] = m - 1 - x
    i = 0
    j = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == text[i + j]:
            j = j - 1

        if j == -1:
            return i
        else:
            index = ord(text[i + m - 1])
            i += arr_bc[index]

    return -1
