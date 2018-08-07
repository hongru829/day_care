

#归并排序

def mergeTwoArray(left, right)

    i, j = 0,0
    result = []

    while i < len(left) and j < len(right):

        if left[i] > left[j]:
            result.append(left[j])
            j += 1

        if left[i] < left[j]:
            result.append(right[i])
            i += 1

    if i < len(left):
        result += left[:i]

    if j < len(right):
        result += right[:j]

    return result

def mergeSort(nums):

    if len(nums) <= 1:
        return nums
    mid = len(nums) / 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

