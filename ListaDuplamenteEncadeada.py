# Maico W. S. Santos

class ListNode:
    def __init__(self, data, antNode = None, nextNode = None):
        self.data = data
        self.antNode = antNode
        self.nextNode = nextNode

    def getData(self):
        return self.data
    def setData(self, val):
        self.data = val
    def getNextNode(self):
        return self.nextNode
    def setNextNode(self, val):
        self.nextNode = val
    def getAntNode(self):
        return self.antNode
    def setAntNode(self, val):
        self.antNode = val

class DoublyLinkedListIterator:
    def __init__(self, firstNode = None):
        self.firstNode = firstNode
        self.lastNode = firstNode
        self.iterator = firstNode
        self.size = 1
    
        if(not self.firstNode):
            self.size = 0

    def getSize(self):
        return self.size
    def get_firstNode(self):
        return self.firstNode
    def get_lastNode(self):
        return self.lastNode
    def get_iterator(self):
        return self.iterator

    def setSize(self, size):
        self.size = size
    def set_firstNode(self, firstNode=None):
        self.firstNode = firstNode
    def set_lastNode(self, lastNode= None):
        self.lastNode = lastNode
    def set_iterator(self, iterator=None):
        self.iterator = iterator

    #Adiciona 1 nó depois do iterador. Iterador passa a apontar o novo nó.
    def addNode(self, data):
        Iterator = self.get_iterator()
        if(Iterator != None):
            ItNextNode = Iterator.getNextNode()
            LastNode = self.get_lastNode()
            Size = self.getSize()
            novoNo = ListNode(data,Iterator,ItNextNode)

            if(ItNextNode != None):
                ItNextNode.setAntNode(novoNo)

            if(Iterator == LastNode):
                self.set_lastNode(novoNo)

            Iterator.setNextNode(novoNo)
            self.set_iterator(novoNo)
            sekf,setSize(Size + 1)

thenode = ListNode(10)

thelist = DoublyLinkedListIterator(thenode)

thelist.addNode(5)

print(thelist.getSize())