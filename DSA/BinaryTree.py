class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Btree:
    def __init__(self):
        self.root=None
    def Add(self,root,data):
        if root==None:
            node=Node(data)
            return node
        if data<root.data:
            root.left=self.Add(root.left,data)
        else:
            root.right=self.Add(root.right,data)
        return root
    def Insert(self,data):
        self.root=self.Add(self.root,data)

    def Inorder(self,root):
        if root==None:
            return
        else:
            self.Inorder(root.left)
            print(root.data,end=" ")
            self.Inorder(root.right)
    def In(self):
        self.Inorder(self.root)
        print()
    def Lev(self,root,k):
        if root is None:
            return
        if k==0:
            print(root.data,end=" ")
        else:
            self.Lev(root.left,k-1)
            self.Lev(root.right,k-1)
    def Level(self,k):
        self.Lev(self.root,k)
        print()

    def Heig(self,root):
        if root is None:
            return 0
        else:
            return max(self.Heig(root.left),self.Heig(root.right))+1
    def Height(self):
        print(self.Heig(self.root))
    def Level_order(self):
        for i in range(self.Heig(self.root)):
            print(f"Level order {i} :-",end=' ')
            self.Level(i)
        print()
    def arr_insert(self,arr):
        for i in range(len(arr)):
            self.Insert(arr[i])
    def max_ele(self,root):
        if root is None:
            return 0
        else:
            return max(root.data,max(self.max_ele(root.left),self.max_ele(root.right)))
    def print_max(self):
        print("Maximum element in Btree is ",self.max_ele(self.root))
b=Btree()
arr=[10,7,5,9,15,13,17]
b.arr_insert(arr)
# b.In()
b.print_max()
# b.Level(0)
# b.Height()
# b.Level_order()