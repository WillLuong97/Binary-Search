#This python program is the solution for Leetcode 61: Rotate List 

#Prolblem statement: 

'''
Given a linked list, rotate the list to the right by k places, where k is a non-negative. 

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

'''



#Linked list node structure: 
class ListNode:
    def __init__(self, val):
        self.val = val          #assign data
        self.nextNode = None    #Initialize next as null

#Linked list stucture: 
class LinkedList:
    #every linkedlist will start out with a head node
    def __init__(self):
        self.head = None #Head node will be initialize as None
    
    #function to insert a node into a linked list
    def insertNode(self, new_data):
        #create a new node: 
        newNode = ListNode(new_data)
        
        #Structure of the linked list: NEW -> HEAD
        newNode.nextNode = self.head

        #head node would now become the new node
        self.head = newNode

    #function to print out the linked list: 
    def printNode(self):
        current = self.head
        while current:
            print(current.val)
            current = current.nextNode
    #function to rotate the linked list by K times
    def rotateRight(self, head, k):
        #check to see if head is null or not: 
        if not head or not head.nextNode:
            return head

        current = head
        lastNode = previousNode = None

        #Find the lenght of the linked list: 
        list_length = 0
        p = head
        while p: 
            list_length += 1
            p = p.nextNode

        #Update K after each rotation
        k = k % list_length

        #no rotation needed to be made
        if k == 0:
            return head

        count = 0
        while current:
            #keep track of the node right before the rotation
            if count < list_length - k:
                previousNode = current
                count += 1


            #keep track of the last node in the linked list to rewire it back to the front at the end
            if not current:
                previousNode = current

            current = current.nextNode
        
        start = previousNode.nextNode
        previousNode.nextNode = None
        lastNode.next = head

        return start
        
        
    
    

def main():
    linkedList = LinkedList()
    #pushing element into a linked list
   
    linkedList.insertNode(5)
    linkedList.insertNode(4)
    linkedList.insertNode(3)
    linkedList.insertNode(2)
    linkedList.insertNode(1)
    headNode = linkedList.head
    
    print("Here is the test linked list: ")
    linkedList.printNode()

    print(f"Here is the linked list length: ", linkedList.rotateRight(headNode, 2))

    
main()
    