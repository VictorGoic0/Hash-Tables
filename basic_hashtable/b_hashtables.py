
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class ListNode:
  def __init__(self, value, prev=None, _next=None):
    self.value = value
    self.prev = prev
    self.next = _next

  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def remove_from_head(self):
    current_head = self.head
    self.delete(self.head)
    self.head = current_head.next
    return current_head.value

  def add_to_tail(self, value):
    if self.tail:
      current_tail = self.tail
      self.tail.insert_after(value)
      self.tail = ListNode(value, current_tail)
      current_tail.next = self.tail
    else:
      self.tail = ListNode(value)
      self.head = self.tail
    self.length += 1

  def delete(self, node):
    if node.prev == None:
      self.head = node.next
    elif node.next == None:
      self.tail = node.prev
    node.delete()
    self.length -= 1
    if (self.length == 0):
      self.head = None
      self.tail = None



class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string):
    hashed = 5381
    byte_array = string.encode('utf-8')
    for byte in byte_array:
        hashed = ((hashed * 33) ^ byte) % 0x100000000
    return hashed

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    hashed = hash(key)
    index = hashed % hash_table.capacity
    if index in hash_table.storage:
        current_bucket = hash_table.storage[index]
        new_pair = Pair(key, value)
        current_bucket.add_to_tail(new_pair)
    else:
        new_pair = Pair(key, value)
        new_bucket = DoublyLinkedList()
        new_bucket.add_to_tail(new_pair)
        hash_table.storage[index] = new_bucket


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed = hash(key)
    index = hashed % hash_table.capacity
    if index in hash_table.storage:
        if hash_table.storage[index].length == 1:
            hash_table.storage[index] = None
        else:
            # loop through, look for the key
            current_node = hash_table.storage[index].head
            found_key = False
            while current_node:
                if current_node.value.key == key:
                    hash_table.storage[index].delete(current_node)
                    found_key = True
                    break
                else:
                    current_node = current_node.next
            if not found_key:
                print("Warning: Key not found")
    else:
        print("Warning: Key not found")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashed = hash(key)
    index = hashed % hash_table.capacity
    if index in hash_table.storage:
        current_node = hash_table.storage[index].head
        found_key = False
        while current_node:
            if current_node.value.key == key:
                return current_node.value.value
            else:
                current_node = current_node.next
        if not found_key:
            return None
    else:
        return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
