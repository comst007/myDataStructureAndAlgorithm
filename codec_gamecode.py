def encodeGameCode(val:str):
    n = len(val)
    if not n:
        return ""
    elif n == 1:
        return "{}{}".format(1, val)
    res = ""
    cur_ch = val[0]
    cnt_ch = 1
    for i in range(1, n):
        if val[i] == cur_ch:
            cnt_ch += 1
        else:
            res = "{}{}{}".format(res, cnt_ch, cur_ch)
            cur_ch = val[i]
            cnt_ch = 1

    res = "{}{}{}".format(res, cnt_ch, cur_ch)
    return res

def decodeGameCode(val:str):
    res = []
    n = len(val)
    if not n:
        return []
    if n % 2 != 0:
        return []
    for i in range(0, n, 2):
        cur_ch = val[i + 1]
        cnt_ch = val[i]
        cur_arr = [cur_ch] * cnt_ch
        res.extend(cur_arr)

    return res

    return []