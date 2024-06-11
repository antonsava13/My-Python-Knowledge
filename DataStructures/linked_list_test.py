import unittest
import linked_list as ll

class TestLinkedList(unittest.TestCase):

    def test_Node(self):
        head_node = ll.Node(0)

        node = head_node

        for i in range(1, 10):
            new_node = ll.Node(i)
            node.next = new_node
            node = node.next

        result = []
        node = head_node
        while node.next is not None:
            result.append(node.data)
            node = node.next
        result.append(node.data)
        result.append("None")
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'None'])

    def test_empty_LinkedList(self):
        llist = ll.LinkedList()
        self.assertEqual(str(llist), "LinkedList(['None'])")

    def test_LinkedList_with_one_node(self):
        llist = ll.LinkedList()
        llist.head = ll.Node(0)
        llist.head.next = ll.Node(1)
        self.assertEqual(str(llist), "LinkedList([0, 1, 'None'])")

    def test_should_append_right_toLinkedList(self):
        llist = ll.LinkedList()
        llist.append(0)
        llist.append(13)
        llist.append(15)
        self.assertEqual(str(llist), "LinkedList([0, 13, 15, 'None'])")

    def test_should_initiate_LinkedList_with_list(self):
        llist = ll.LinkedList([1, 5, 6, 10, 13])
        self.assertEqual(str(llist), "LinkedList([1, 5, 6, 10, 13, 'None'])")

    def test_should_append_left_toLinkedList(self):
        llist = ll.LinkedList()
        llist.appendleft(7)
        llist.appendleft("b")
        llist.appendleft(22)
        self.assertEqual(str(llist), "LinkedList([22, 'b', 7, 'None'])")

    def test_should_be_itterable(self):
        old_list = [3, 25, 4, 6, 8]
        llist = ll.LinkedList(old_list)
        self.assertTrue(hasattr(llist, "__iter__"))
        new_list = [x for x in llist]
        self.assertEqual(new_list, old_list)

    def test_should_remove_first_Value(self):
        # Try removing from empty list
        llist = ll.LinkedList()
        llist.remove_value(1)
        self.assertEqual(list(llist), [])

        # Try to remove the only value
        llist = ll.LinkedList(1)
        llist.remove_value(1)
        self.assertEqual(list(llist), [])

        # Try to remove the first value in long lliest
        old_list = [3, 25, 4, 6, 8, 25]
        llist = ll.LinkedList(old_list)
        llist.remove_value(3)
        self.assertEqual(list(llist), [25, 4, 6, 8, 25])

        # Rmoving eliment in the middle
        llist.remove_value(6)
        self.assertEqual(list(llist), [25, 4, 8, 25])

        # Rmoving Tail Node
        llist.remove_value(25)
        llist.remove_value(25)
        self.assertEqual(list(llist), [4, 8])


    def test_should_remove_dublicates(self):
        old_list = [3, 3, 3, 25, 4, 6, 8, 12, 11, 3, 25, 4, 3]
        llist = ll.LinkedList(old_list)
        llist.remove_dublicates()
        self.assertEqual(list(llist), [3, 25, 4, 6, 8, 12, 11])

        old_list = [3, 3, 3, 3, 3, 3, 3]
        llist = ll.LinkedList(old_list)
        llist.remove_dublicates()
        self.assertEqual(list(llist), [3])

if __name__ == "__main__":
    unittest.main()