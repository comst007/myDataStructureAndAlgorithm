def select(nums: list, res_cur: list, res_total: list):
    cnt_nums = len(nums)
    if not cnt_nums:
        res_total.append(res_cur[:])
    else:
        last_index = -1
        for i in range(cnt_nums):
            if last_index == -1 or nums[last_index] != nums[i]:
                last_index = i
                sub = nums[:]
                res_cur.append(nums[i])
                sub.pop(i)
                select(sub, res_cur, res_total)
                res_cur.pop()


def pernumtation_no_repeat(nums:list):
    res = []
    if not nums:
        return []
    select(nums, [], res)
    return res

def permutation_has_repeat(nums:list):
    res = []
    if not nums:
        return []
    nums_sorted = sorted(nums)
    select(nums_sorted, [], res)
    return res