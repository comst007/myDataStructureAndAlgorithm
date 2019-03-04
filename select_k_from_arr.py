import pprint

# arr has no repeat element
def select_k_ret_cnt(arr:list, k):
    if not arr:
        return 0
    arr_len = len(arr)
    if k == 1:
        return arr_len
    if k == arr_len:
        return 1
    return select_k_ret_cnt(arr[1:], k) + select_k_ret_cnt(arr[1:], k - 1)

# arr has no repeat element
def select_k_ret_arr(arr:list, k):
    res_arr = []
    if not arr:
        return []
    arr_len = len(arr)
    if k == 1:
        return [(x,) for x in arr]
    if k == arr_len:
        return [tuple(arr)]

    res1 = select_k_ret_arr(arr[1:], k - 1)
    res2 = select_k_ret_arr(arr[1:], k)
    for x in res1:
        cur = (arr[0],) + x
        res_arr.append(cur)
    res_arr.extend(res2)
    return res_arr





