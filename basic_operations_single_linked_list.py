class Node:                             #class to create the structure of the Node
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class CreateLinkedList():
    def __init__(self,headval=None):       #function to initialize the head Node
        self.headval = headval

    def listprint(self):                   #function to traverse the linked list
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    
    def begin_add(self,element):           #function to add element at the beginning of the linked list
        beg = Node(element)
        beg.nextval = self.headval
        self.headval = beg
        printval = self.headval
    
    def end_add(self,element):          #function to add element at the end of the linked list
        end = Node(element)
        printval = self.headval
        if not printval:
            self.headval = end
            return
        while printval.nextval:
            #print (printval.dataval)
            printval = printval.nextval
        printval.nextval= end
        printval = self.headval
        
    def mid_add(self,mid_node,element):    #function to add node in the middle of the linked list after the mid_node mentioned
        if mid_node == '':                  #mid_node is the input after which the new node with the value 'element' will be created
            print("No mid node exists")
            return
        printval = self.headval      
        while printval is not None:        #check if mid_node value mentioned in input is correct till the end of the linked list
            if printval.dataval == mid_node:
                new_node= Node(element)
                new_node.nextval = printval.nextval
                printval.nextval = new_node
                return
            printval =printval.nextval
        print("Element Not Found")
        return
    
    def beg_mid_add(self,mid_beg_node,element): #function to add node in the middle of the linked list before the mid_node mentioned
        if mid_beg_node == '':
            print("No mid node exists")
            return
        printval = self.headval
        if printval.dataval == mid_beg_node:
            new_node = Node(element)
            new_node.nextval = printval
            self.headval = new_node
            return
        while printval.nextval is not None:
            if (printval.nextval).dataval == mid_beg_node:
                new_node= Node(element)
                new_node.nextval = printval.nextval
                printval.nextval = new_node
                return
            printval =printval.nextval
        print("Element Not Found")
        return

    def delete(self,element):
        printval = self.headval
        if element == printval.dataval:
            if printval.nextval is not None:
                self.headval = printval.nextval
            else:
                self.headval = None
            return
        else:
            while printval.nextval is not None:
                #if printval.nextval is not None:
                if (printval.nextval).dataval == element:
                    print("found")
                    printval.nextval = (printval.nextval).nextval
                    return
                printval = printval.nextval
            print("Element Not Present")
            return


list = CreateLinkedList(Node("10"))
list.headval.nextval = Node('100')
list.mid_add('10','20')
list.listprint()
list.mid_add('dummy_value','dv')
list.listprint()
list.beg_mid_add('dummy_value','dv')
list.listprint()
list.beg_mid_add('10','5')
list.beg_mid_add('5','0')
list.beg_mid_add('100','90')
list.end_add('120')
list.listprint()
list.delete('')
list.delete('120')
print("FINAL OUTPUT")
list.listprint()
