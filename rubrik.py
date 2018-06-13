

# 1 clone ListNode
def cloneList(self, RandomListNode):

    map = {}
    dummyNode = RandomListNode(0)

    current, head = RandomListNode, dummyNode

    while current:

        newNode = RandomListNode(current.val)
        head.next = newNode
        map[current] = newNode
        current = current.next
        head = head.next

    current = RandomListNode

    while current:
        if current.random:
            map[current].randome = map[current.random]
            current = current.next


    return dummyNode.next

# maximum subarray sum

def maximumSubarray(self, nums):

    dp = [0] * len(nums)

    for i in range(len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        res = max(res, dp[i])

    return res


