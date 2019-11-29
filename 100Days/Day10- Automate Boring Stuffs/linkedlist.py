
class Node():
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next


class LinkedList(object):

    def __init__(self):
        self._head = None
    
    @property
    def head(self):
        return self._head
    
    def add(self, node):
        if self._head == None:
            self._head = node
        else:
            next_node = self._head
            while next_node != None:
                current = next_node
                next_node = next_node.next
            current.next = node
    
    def add_beginning(self,node):
        if self._head is None:
            self._head = node
        else:
            node.next = self._head
            self._head = node
    
    def print_list(self):
        current = self._head
        while current is not None :
            print(current.data)
            current = current.next
        

    def find(self):
        pass
    

if __name__ == '__main__':
    node = Node('hello')
    linkedlist= LinkedList()
    linkedlist.add(node)
    node_1 = Node('next')
    linkedlist.add(node_1)

    linkedlist.print_list()
    linkedlist.add_beginning(Node('baka'))
    linkedlist.print_list()
