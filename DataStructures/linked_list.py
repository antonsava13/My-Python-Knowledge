class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self, nodes=None):

        self.head = None

        if nodes is not None:
            if hasattr(nodes, '__iter__'):
                new_node = Node(nodes[0])
                self.head = new_node
                node = new_node
                for el in nodes[1:]:
                    node.next = Node(el)
                    node = node.next
            else:
                self.head = Node(nodes)


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append((node.data))
            node = node.next
        nodes.append("None")
        return f"LinkedList({nodes})"


    def __iter__(self):
        node = self.head

        while node is not None:
            yield node.data
            node = node.next


    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node


    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def remove_value(self, value):
        """ This function will remove the first node that stores the value. It will not remove
        the consequent Nodes with the same value"""

        node = self.head

        # Removing value from an empty llist
        if node is None:
            return

        # Removing value from head
        if self.head.data == value:
            self.head = node.next

        # Removing value anywhere but from the head
        else:
            while node.next is not None:
                if node.next.data == value:
                    node.next = node.next.next

                if node.next is None:
                    node = node
                else:
                    node = node.next



    def remove_dublicates(self):

        if self.head.next is not None:
            # The list has at least two members
            node = self.head
            while node.next is not None:
                runner = node
                while runner.next is not None:
                    if node.data == runner.next.data:
                        runner.next = runner.next.next

                        # It can be the case were runner.next.next is also a dublicate
                    if runner.next is not None and runner.next.data != node.data:
                        runner = runner.next
                if node.next is not None:
                    node = node.next








if __name__ == "__main__":
    pass





