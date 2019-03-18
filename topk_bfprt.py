def sort_insert(arr:list, l:int, h:int):
    if l >= h:
        return
    for i in range(l + 1, h + 1):
        if arr[i] >= arr[i - 1]:
            continue
        j = i - 1
        tmp = arr[i]
        while j >= 0 and arr[j] > arr[i]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = tmp


def findMid(arr:list, l:int, h:int):
    if l == h:
        return l
    n = h - l + 1
    j = 0
    for i in range(l, h - 5, 5):
        sort_insert(arr, i, i + 4)
        arr[l + j] = arr[i + 2]
        j += 1


    last_cnt = n % 5
    sort_insert(arr, h - last_cnt + 1, h)
    arr[l + j] = arr[h - last_cnt // 2]
    if j == 0:
        return l
    return findMid(arr,l, l + j)


def partion(arr: list, l: int, h: int):
    p = arr[l]
    start = l
    end = h
    while start < end:
        while start < end and arr[end] >= p:
            end -= 1

        arr[start] = arr[end]
        while start < end and arr[start] < p:
            start += 1
        arr[end] = arr[start]

    arr[start] = p
    return start

def topk_bfprt(arr:list, l:int, h:int, k:int):
    p = findMid(arr, l, h)
    p = partion(arr, l, h)
    if k == p:
        return arr[p]
    if k < p:
        return topk_bfprt(arr, l, p - 1, k)
    return topk_bfprt(arr, p + 1, h, k - p)

