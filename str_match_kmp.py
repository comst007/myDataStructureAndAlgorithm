def kmp_next(line):
    next_j = [0] * len(line)
    next_j[0] = -1
    cnt = len(line)
    if cnt == 1:
        return next_j
    next_j[1] = 0
    i = 2

    k = 0
    while i < cnt:
        k = next_j[i - 1]

        while k != -1 and line[i - 1] != line[k]:
            k = next_j[k]

        if k == -1:
            next_j[i] = 0
         else:
             next_j[i] = k + 1
             i += 1

    return next_j


def strStr(haystack: str, needle: str, start):
    if start >= len(str):
        return -1
    if not haystack:
        if not needle:
            return 0
        else:
            return -1
    if not needle:
        return 0
    left_len = len(haystack) - start
    right_len = len(needle)

    if left_len < right_len:
        return -1
    next_pos = kmp_next(needle)

    i = 0
    j = 0
    while i < left_len and j < right_len:
        if j == -1 or haystack[i + start] == needle[j]:
            i += 1
            j += 1
        else:
            j = next_pos[j]

    if j < right_len and i == left_len:
        return -1
    elif j == right_len and i < left_len:
        return i - right_len + start
    else:
        return i - right_len + start


def findAll(haystack: str, needle: str):
    len_needle = len(needle)
    if not len_needle:
        return []
    pos_arr = []
    pos_cur = 0
    start = 0
    while True:
        pos_cur = strStr(haystack, needle, start)
        if pos_cur == -1:
            break
        else:
            pos_arr.append(pos_cur)
            start = pos_cur + len_needle

    return pos_arr
