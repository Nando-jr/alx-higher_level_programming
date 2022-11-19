#!/usr/bin/python3
"""Node Class and SinglyLinkedList class"""


class Node:
    """class Node that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set Data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node"""
        if not (value is None or type(value) is Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class SinglyLinkedList that defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        a = ""
        pr = self.__head
        while pr:
            a += str(pr.data)
            if pr.next_node:
                a += "\n"
            pr = pr.next_node
        return a

    def sorted_insert(self, value):
        pr = self.__head
        while pr:
            if pr.data > value:
                break
            pr_prev = pr
            pr = pr.next_node
        new_node = Node(value, pr)
        if pr == self.__head:
            self.__head = new_node
        else:
            pr_prev.next_node = new_node
