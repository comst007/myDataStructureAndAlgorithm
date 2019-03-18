def insertSharp(s:str):
    res = "#".join(s)
    return "#" + res + "#"

def manacher(s:str):
    n = len(s)
    if not n:
        return 0
    if n == 1:
        return 1
    s_sharp = insertSharp(s)
    n_sharp = len(s_sharp)
    c = -1
    r = -1
    maxlen = -1
    parr = [0] * n_sharp
    for i in range(n_sharp):
        if i < r:
            c_i = c * 2 - i
            if c_i - parr[c_i] > c - r:
                parr[i] = parr[c_i]
                maxlen = max(parr[i], maxlen)
                if i + parr[i] > r:
                    r = i + parr[i]
                    c = i
            else:
                start = r - i + 1
                while i - start >= 0 and i + start < n_sharp and s_sharp[i - start] == s_sharp[i + start]:
                    start += 1

                parr[i] = start - 1
                maxlen = max(maxlen, parr[i])
                if i + parr[i] > r:
                    r = i + parr[i]
                    c = i
        else:
            start = 1
            while i - start >= 0 and i + start < n_sharp and s_sharp[i - start] == s_sharp[i + start]:
                start += 1

            parr[i] = start - 1
            maxlen = max(maxlen, parr[i])
            if i + parr[i] > r:
                r = i + parr[i]
                c = i


    return (2 * maxlen + 1) // 2