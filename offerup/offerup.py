

def maximumSubarraySizeEqualsToK(nums, k):

    sum = {}
    cur_sum = 0
    maxLen = 0
    for i in xrange(len(nums)):
        cur_sum += nums[i]

        if cur_sum == k:
            maxLen = i + 1

        if cur_sum - k in sum:
            maxLen = max(maxLen, i -  sum[cur_sum])

        sum[cur_sum]
