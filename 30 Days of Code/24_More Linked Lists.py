class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        cur = None
        if head:
            cur = self.insert(cur, head.data)
        while head.next:
            if head.data == head.next.data:
                head = head.next
            else:
                head = head.next
                cur = self.insert(cur, head.data)
        return cur
''''  #Working solution
        list = [head]
        cur = None
        for node in list:
            if node.next:
                list.append(node.next)
                if node.data == node.next.data:
                    list.remove(node)
                    list.append(node.next)
                else:
                    cur = self.insert(cur, node.data)
                    node = node.next
            else:
                cur = self.insert(cur, node.data)                
        return cur
'''


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 