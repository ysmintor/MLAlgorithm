
class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    # 将二叉树转换为有序双向链表
    def Convert(self, pRootOfTree):
        if pRootOfTree==None:
            return
        self.Convert(pRootOfTree.left)
        if self.listHead==None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead

    # 获得链表的正向序和反向序
    def printList(self, head):
        while head.right:# 正向
            print(head.val, end=" ")
            head = head.right

        # 最后的一个元素单独输入
        print(head.val)

        while head: # 逆向
            print(head.val, end= " ")
            head = head.left


    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self, pre, tin):
        if len(pre)==0 | len(tin)==0:
            return None

        root = TreeNode(pre[0])
        for order,item in enumerate(tin):
            if root .val == item:
                root.left = self.getBSTwithPreTin(pre[1:order+1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order+1:], tin[order+1:])
                return root


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

if __name__ == '__main__':
    solution = Solution()
    preorder_seq = [4,2,1,3,6,5,7]
    middleorder_seq = [1,2,3,4,5,6,7]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    head = solution.Convert(treeRoot1)
    solution.printList(head)

            #      4
            #    /   \
            #   2     6
            #  / \   / \
            # 1   3 5   7
