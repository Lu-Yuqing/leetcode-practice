# https://leetcode.com/problems/lru-cache/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: hashmap + doubly linked list
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key -> node
        self.head = Node(-1, -1)  # most recently used
        self.tail = Node(-1, -1)  # least recently used
        self.head.next, self.tail.prev = self.tail, self.head

    # remove the node from doubly linked list
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    # insert to the start
    def add_to_head(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node

    def move_to_head(self, node):
        self.remove(node)
        self.add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.move_to_head(node)  # UPDATE MOST RECENTLY USED
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
        else:
            newnode = Node(key, value)
            self.cache[key] = newnode
            self.add_to_head(newnode)

            if len(self.cache) > self.cap:
                deletnode = self.tail.prev
                self.remove(deletnode)
                del self.cache[deletnode.key]

