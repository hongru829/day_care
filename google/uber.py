

#1. 面试官名字看起来是东欧或者俄罗斯人。
#   题目是给一个list of word， 每个word 叫做root word
#   然后还有个input string 是sentence，
#   要求是把sentence 中的单词如果有root word 是单词的prefix， 就把这个单词替换成root word。最后返回替换后的sentence
#   例子：
#       root word ["abc", "car", "race"].
#       sentence "abcde cars ca bounse"
#       return: "abc car ca bounse"

# 另外不会有某个root word 是另外一个root word的prefix. 当晚收到onsite

class TrieNode:
    def __init__(self):
        self.val = val
        self.children = dict()
        self.isEnd = False

class Trie(object):

    def __init__(self, words):

        self.root = TrieNode()


    def insert(self, word):
        curNode = root

        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]
        curNode.isEnd = True


    def search(self, word):
        curNode = root
        prefixofthisWord = ''
        for i in range(len(word)):
            if word[i] in curNode.children:
                curNode.children[word[i]] = TrieNode()
            else:
                if i >= 0 && curNode.isEnd == True:
                    return curNode.val
                else:
                    return ""
            curNode = curNode.children[word[i]]
            curNode.val += word[i]
        if i >= 0 && curNode.isEnd == True:
            return curNode.val
        else:
            return ""

tt = Tire()

for word in words:
    tt.insert(word)

splitedWords = sentence.split(' ');

for w in splitedWords:
    res = []
    if tt.search(w) != '':
        res.append(tt.search(w))
    else:
        res.append(w)

return " ".join(res)

# Interval List A：<1,3> <5,7>. 牛人云集,一亩三分地
# B: <4,6>. Waral 博客有更多文章,
# 输出交集 <5,6>. visit 1point3acres for more.
# 输出并集 <1,7> 要求是如果前一个interval的end是后一个的start-1要合并。多谢中国大哥放水。



# http://www.1point3acres.com/bbs/thread-200291-1-1.html
# 第一轮一个小美engineer面的。
# Write two functions to index the documents and search documents.
# void Index(Document doc);
# List<Document> search(Query query);
# Follow up: the query supports Boolean operations, like AND, OR, NOT etc in the query. (No time to do this.)
# 然后recruiter说面的不错，再来一轮。不错的话不应该是直接onsite吗。。.本文原创自1point3acres论坛

# 第二次是经理面的。这经理是一个startup的CTO，公司被Uber收购了。就过来当manager了。聊了半天。然后上题：LC17. Letter Combinations of a Phone Number
# The code need to be runnable with main function and test cases. I did both of them correctly.
# 然后被拒，还是有点吃惊。可能写的太慢了，可能花了几分钟调一个bug，或者他根本就没看上我的背景





# 3sum but give you three sorted array

# first method

def findTargetIn3SortedArray(a1, a2, a3):

    for i in range(len(a1)):
        for j in range(len(a2)):
            for k in range(len(a3)):
                if a1[i] + a2[j] + a3[k] == target:
                    return True
    return False

# second method:

def findTargetIn3SortedArray(num1, nums2, nums3):

    dic = colleciton.defaultdic(int)

    for i in range(len(nums1))
        dic[num] = i

    for i in range(len(nums2)):
        for j in range(len(nums3)):
            if target - nums[i] - nums[j] in dic:
                return True
    return False

# deserilize and sealize tree

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
            res.append(str(node.val) if node else "#")
        # strip left ','
        return ",".join(res).strip(',')


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = []
        for i in data.split(","):
            if i != '#':
                nodes.append(TreeNode(i))
            else:
                nodes.append(None)

        queue = [nodes[0]]
        index = 1
        while queue:
            node = queue.pop(0)
            if index < len(nodes) and nodes[index]:
                node.left = nodes[index]
                queue.append(nodes[index])
            if index + 1 < len(nodes) and nodes[index+1]:
                node.right = nodes[index+1]
                queue.append(nodes[index+1])
            index += 2

        return nodes[0]









