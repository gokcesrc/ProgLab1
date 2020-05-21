#!/usr/bin/env python
# coding: utf-8

# In[56]:


class Node:
    def __init__(self,key): #Constructor özel br fonksiyon
        self.left=None
        self.right=None
        self.val=key


# In[57]:


def insert(root,node):
    if root is None:
        root=node
    else:
        if root.val<node.val:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)


# In[58]:


def inorder(root): #rootu ortaya alarak diziyi yazıyor.
    if root:#önce sol sonra kendisi sonra sağdakini yaz mantığı vardır.
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)


# In[59]:


r=Node(50) #Node türünden bir yapı oluşturduk ve bunu r değişkenine atadık.


# In[60]:


insert(r,Node(30))


# In[61]:


insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))


# In[62]:


inorder(r)


# In[63]:


def search(root,key):
    #Base Cases: root is null or key is present at root
    if root is None or root.val==key:
        return root
    
    #Key is greater than root's key
    if root.val < key:
        return search(root.right,key)

    #Key is smaller than root's key
    return search(root.left,key)


# In[64]:


result=search(r,20)
result


# In[65]:


result.val


# In[66]:


def minValueNode(node):
    current=node
    
    #Loop down to find the Leftmost leaf
    while(current.left is not None):
        current=current.left
        
    return current

#Given a binary search tree and a key this function
#delete the key and returns the new root
def deleteNode(root,key):
    
    #Base Case
    if root is None:
        return root
    
    #If the key to be deleted is smaller than the root's
    #key then it lies in left subtree
    if key<root.val:
        root.left=deleteNode(root.left,key)
        
    #If the key to be delete is greater than the root's key
    #then it lies in right subtree
    elif(key > root.val):
        root.right = deleteNode(root.right,key)
        
    #If key is same as root's key, then this is the node to be deleted
    else:
        
        #Node with one child or no child
        if root.left is None:
            temp = root.right
            root=None
            return temp
        
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        
        #Node with two childresn: Get the inorder successor
        #(smallest in the right subtree
        temp=minValueNode(root.right)
        
        #Copy the inorder successor's content to this node
        root.key=temp.val
        
        #Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)
        
    return root


# In[67]:


root=deleteNode(r,20)
insert(root,Node(250))
print("Inorder traversal of the modified tree")
inorder(root)


# In[ ]:




