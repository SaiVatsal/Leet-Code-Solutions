class Node:
    def __init__(self):
        self.child = [None] * 10
        self.isEnd = False
class Solution:
    def insert(self, word, root):
        temp = root
        for ch in word:
            idx = ord(ch) - ord('0')
            if temp.child[idx] is None:
                temp.child[idx] = Node()
            temp = temp.child[idx]
        temp.isEnd = True


    def check(self, string, root): 
        temp = root 
        idx = 0 

        while idx < len(string): 
            i = ord(string[idx]) - ord('0')  

            if temp.child[i] is not None: 
                temp = temp.child[i] 
                idx += 1 
            else:
                break

        return idx

    def longestCommonPrefix(self, arr1, arr2):
        root = Node()

        for x in arr2:
            self.insert(str(x), root)

        ans = 0

        for x in arr1:
            ans = max(ans, self.check(str(x), root))

        return ans