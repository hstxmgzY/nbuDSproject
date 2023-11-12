# -*- coding: utf-8 -*-
# @Time    : 2023/4/7
# @Author  : @yaowanxin
# @Software: PyCharm
# @description: hhhhhh

class tree_node:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class bst_tree:

    # 查找函数
    def bst_search(self, root, key):
        str1 = ""
        # 当访问到最后得到的是None，说明元素不存在查找树上
        if root == None:
            print(None)
            print("找不到！")
            return False
        # 当前结点值等于key时查找成功
        if root.data == key:
            print(root.data)
            print("找到了！")
            return True
        # 当结点值小于key时，说明目标有可能存在右子树
        elif root.data < key:
            str1 = str1 + str(root.data) + " ->rchild "
            print(str1, end="")
            return self.bst_search(root.rchild, key)

        # 当结点值大于key时，说明目标有可能存在左子树
        if root.data > key:
            str1 = str1 + str(root.data) + " ->lchild "
            print(str1, end="")
            return self.bst_search(root.lchild, key)

    # 二叉查找数元素插入
    # 根据二叉查找树的左小右大的特性，当 当前结点值大于key则说明值插入到左子树，否则在右子树
    # 当root == None时，说明就是插入的位置
    def bst_insert(self, root, key):
        # 当值为None，创建新结点
        if root == None:
            root = tree_node(key)
        # 存在时
        elif root.data == key:
            print("此元素已存在，不必再次插入！")
            pass
        # 当结点值小于key时，说明要往右子树插
        elif root.data < key:
            root.rchild = self.bst_insert(root.rchild, key)
        # 当结点值大于key时，说明要往左子树插
        elif root.data > key:
            root.lchild = self.bst_insert(root.lchild, key)
        return root

    ## 寻找二叉查找树以root为根节点的最大权值
    def bst_search_max(self, root):
        if root.rchild:
            return self.bst_search_max(root.rchild)
        else:
            return root

    # 删除
    # 删除根节点的处理方法，为了保证删除根节点后依旧是一颗完整的二叉查找树，这里可以用左子树中的最大值和右子树中的最小值来代替根节点，然后在子树中删除相应的叶节点
        # 1）若root值为None, 说明二叉树中不存在要删除的值，直接返回
        # 2）如果root值大于key，key可能在左子树，递归
        # 3）如果root值小于key，key可能在右子树，递归
        # 4）若root值刚好是key，说明已经找到了要删除的结点，进行删除处理操作：
            # a) 如果root没有左右子树了，直接删除结点，并且返回
            # b) 如果root还有左子树，则寻找左子树中的最大值，用于替换root，然后在左子树中删除结点
            # c) 如果root还有右子树，则寻找右子树的最小树，用于替换root，然后在右子树中删除结点
    def bst_delete(self, root, key):
        # 若root值为None, 说明二叉树中不存在要删除的值，直接返回
        if root is None:
            print("二叉树中不存在要删除的值: " + str(key))
            return root
        # 如果key比root的值小，那么要在root的左子树中删除
        if key < root.data:
            root.lchild = self.bst_delete(root.lchild, key)

        # 如果key比root的值大，那么要在root的右子树中删除
        elif key > root.data:
            root.rchild = self.bst_delete(root.rchild, key)

        # 如果key等于root的值，那么要删除root节点
        else:
        # 如果root没有左右子树，则直接删除root
            if root.lchild is None and root.rchild is None:
                root = None

        # 如果root只有左子树或右子树，则用子树节点代替root节点
            elif root.lchild is None:
                root = root.rchild
            elif root.rchild is None:
                root = root.lchild

        # 如果root既有左子树又有右子树，则用左子树的最大节点或右子树的最小节点代替root节点
            else:
                # 找到左子树的最大节点
                max_node = self.bst_search_max(root.lchild)
                # 将左子树的最大节点的值赋给root节点
                root.data = max_node.data
                # 在左子树中删除最大节点
                root.lchild = self.bst_delete(root.lchild, max_node.data)
        return root

    # xm
    def bst_mid_scan(self, root):
        if root is None:
            return
        # 遍历左子树
        self.bst_mid_scan(root.lchild)
        # 遍历根节点
        print(root.data, end=',')
        # 遍历右子树
        self.bst_mid_scan(root.rchild)

    #创建二叉查找树
    def bst_create(self, list1):
        if len(list1) != 0:
            root = tree_node(list1[0])
        else:
            return None
        for i in range(1, len(list1)):
            self.bst_insert(root, list1[i])
        return root


if __name__ == '__main__':
    BST = bst_tree()
    print("=============欢迎进入二叉树===============")
    flag1 = int(input("请输入对应操作数字 0：退出，1：开始--"))
    while(flag1 != 0):

        print("===============创建二叉树================")
        list1 = list(map(int, input("请输入用空格分隔的一串数字：").split()))
        root = BST.bst_create(list1)
        flag2 = int(input("请输入对应操作数字 0：退出，1：查询，2：插入，3：删除，4：显示--"))
        while flag2 != 0:
            if flag2 == 1:
                print("================查询  元素===============")
                n = int(input("查询元素："))
                print("在二叉树中查找元素：", n, BST.bst_search(root, n))
            if flag2 == 2:
                print("================插入  元素===============")
                n = int(input("插入元素："))
                BST.bst_insert(root, n)
                BST.bst_mid_scan(root)
                print()
            if flag2 == 3:
                print("================删除  元素===============")
                n = int(input("删除元素："))
                BST.bst_delete(root, n)
            if flag2 == 4:
                print("================中序  显示===============")
                BST.bst_mid_scan(root)
                print()
            flag2 = int(input("请输入对应操作数字 0：退出，1：查询，2：插入，3：删除，4：显示--"))
        flag1 = int(input("请输入对应操作数字 0：退出，1：开始--"))
    print("================再见  👋===============")

