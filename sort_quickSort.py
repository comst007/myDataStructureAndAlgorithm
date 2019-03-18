def sort_quik(arr:list, l:int, h:int):
    if l >= h:
        return
    k = partion(arr, l, h)
    sort_quik(arr, l, k - 1)
    sort_quik(arr, k + 1, h)


def partion(arr:list, l:int, h:int):
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
