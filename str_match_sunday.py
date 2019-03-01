def horspool(text:str, pat:str):
    n = len(text)
    if not n:
        return -1
    m = len(pat)
    if not m:
        return 0
    arr_bc = [m + 1] * 256

    for x in range(m):
        arr_bc[ord(pat[x])] = m - x
    i = 0
    j = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == text[i + j]:
            j = j - 1

        if j == -1:
            return i
        else:
            if i + m >= n:
                return -1
            index = ord(text[i + m])
            i += arr_bc[index]

    return -1
