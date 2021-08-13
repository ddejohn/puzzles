def are_consecutive(nums):
    acc = 0
    for i in range(len(nums)-1):
        acc += abs(nums[i] - nums[i+1])
    return acc == len(nums) - 1


def sliding_slice(nums, start, end):
    if not are_consecutive(nums[start:end+1]) or end+1 > len(nums):
        return nums[start:end], start, end
    return sliding_slice(nums, start, end+1)


def solution(nums):
    res = []
    si = 0
    sf = si + 3

    while True:
        if are_consecutive(nums[si:sf]):
            slc, si, sf = sliding_slice(nums, si, sf)
            res.append(f"{slc[0]}-{slc[-1]}")
            si = sf
            sf = si + 3
        else:
            res.append(str(nums[si]))
            si += 1
            sf = si + 3

        if sf > len(nums):
            if nums[si:]:
                res.extend(map(str,[*nums[si:]]))
            break
    
    res = ",".join(res)
    return res