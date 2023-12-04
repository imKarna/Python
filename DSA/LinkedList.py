class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Link:
    def __init__(self):
        self.head=None
    def Display(self):
        if self.head is None:
            print("Empty Linked List")
            return
        temp=self.head
        while(temp is not None):
            print(temp.data,end=' ')
            if temp.next:
                print("-->",end="")
            else:
                print("")
            temp=temp.next
    def at_head(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        node=Node(data)
        node.next=self.head
        self.head=node
    def add(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=Node(data)
    def index(self,data,ind):
        if ind==0:
            self.at_head(data)
            return
        node=Node(data)
        temp=self.head
        count=0
        while temp:
            if count==ind-1:
                node.next=temp.next
                temp.next=node
            temp=temp.next
            count+=1
    def delete(self,index):
        if index==0:
            self.head=self.head.next
            return
        temp=self.head
        count=0
        while temp.next is not None:
            if count==index-1:
                temp.next=temp.next.next
            temp=temp.next
            count+=1
    def get_from_last(self,ele):
        first=self.head.next
        second=self.head
        for i in range(ele):
            first=first.next
        while first is not None:
            first=first.next
            second=second.next
        print(second.data)


l=Link()
l.add(10)
l.add(20)
l.add(30)
l.at_head(0)
l.index(33,3)
# l.delete(3)
l.Display()
l.get_from_last(3)