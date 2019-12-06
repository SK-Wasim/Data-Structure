class node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        
class mytree:
        
    def insert(self,root,n):
        if root is None:
            root = n
        else:
            if root.val > n.val:
                if root.left is None:
                    root.left = n
                else:
                    self.insert(root.left,n)
            else:
                if root.right is None:
                    root.right = n
                else:
                    self.insert(root.right,n)
                    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
            
    def minValueNode(self,node):
        curr = node
        while curr.left is not None:
            curr = curr.left        
        return curr
    
    def maxValueNode(self,node):
        curr = node
        while curr.right is not None:
            curr = curr.right        
        return curr
    
    def deleteNode(self,root, key):
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
            
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
            
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.minValueNode(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right,temp.val)
            return root
            

r = node(50)
obj = mytree()
obj.insert(r,node(30))
obj.insert(r,node(20))
obj.insert(r,node(40))
obj.insert(r,node(70))
obj.insert(r,node(60))
obj.insert(r,node(80))
obj.inorder(r)
print("-----------------")
print((obj.minValueNode(r)).val)
print("------- Delete Node -----------")
print((obj.deleteNode(r,70)))
print("-----------------")
obj.inorder(r)