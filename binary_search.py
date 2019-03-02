def binarySearch(arr:list, target:int):
    cnt = len(arr)
    if not cnt:
        return -1
    if target > arr[-1] or target < arr[0]:
        return -1
    start = 0
    end = cnt
    mid = 0
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return -1

def lowerBound(arr:list, target:int):
    cnt = len(arr)
    if not cnt:
        return -1
    if target > arr[-1] or target < arr[0]:
        return -1
    start = 0
    end = cnt
    mid = 0
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            end = mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    if arr[start] == target:
        return start
    else:
        return -1

def upperBound(arr:list, target:int):
    cnt = len(arr)
    if not cnt:
        return -1
    if target > arr[-1] or target < arr[0]:
        return -1
    start = 0
    end = cnt
    mid = 0
    while start < end - 1:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            start = mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    if arr[start] == target:
        return start
    else:
        return -1

def lowerAndUpperBound(arr:list, target:int):
    bound_low = lowerBound(arr, target)
    bound_up = upperBound(arr, target)
    return [bound_low, bound_up]

def insertPos(arr:list, target:int):
    cnt = len(arr)
    if not cnt:
        return -1
    if target >= arr[-1]:
        return cnt
    if target <= arr[0]:
        return 0
    start = 0
    end = cnt
    mid = 0
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            start = mid + 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid

    return start


def firstLarge(arr:list, target:int):
    return insertPos(arr, target)

def firstSmall(arr:list, target:int):
    cnt = len(arr)
    if not cnt:
        return -1
    if target > arr[-1]:
        return cnt - 1
    if target <= arr[0]:
        return -1
    start = 0
    end = cnt
    mid = 0
    while start < end - 1:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            end = mid
        elif arr[mid] < target:
            start = mid
        else:
            end = mid

    return start

arr1 = [1,3,3,5,8]
target1 = 3

arr2 = [1,2,4,5,7,8,8,9,10]
target2 = 6

print(arr1)
print("pos", target1, binarySearch(arr1, target1))

print("lowerbound", target1, lowerBound(arr1, target1))

print("upperBound", target1, upperBound(arr1, target1))

print("lowerAndUpperBound", target1, lowerAndUpperBound(arr1, target1))

print("insertPos", target1, insertPos(arr1, target1))

print("firstLarge", target1, firstLarge(arr1, target1))

print("firstSmall", target1, firstSmall(arr1, target1))


print("-" * 30)
print(arr2)
print("pos", target2, binarySearch(arr2, target2))

print("lowerbound", target2, lowerBound(arr2, target2))

print("upperBound", target2, upperBound(arr2, target2))

print("lowerAndUpperBound", target2, lowerAndUpperBound(arr2, target2))

print("insertPos", target2, insertPos(arr2, target2))

print("firstLarge", target2, firstLarge(arr2, target2))

print("firstSmall", target2, firstSmall(arr2, target2))