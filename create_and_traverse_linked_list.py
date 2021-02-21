class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class CreateLinkedList:
    def __init__(self,headval):
        self.headval = headval

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list = CreateLinkedList(Node("Start"))
#list.headval = Node("Mon")
e2 = Node("Mid")
e3 = Node("End")
list.headval.nextval = e2
e2.nextval = e3

list.listprint()
