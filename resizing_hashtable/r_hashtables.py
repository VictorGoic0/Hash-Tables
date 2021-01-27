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

class Pair:
  def __init__(self, key, value):
    self.key = key
    self.value = value

class HashTable:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = [None] * capacity
    self.pairs = 0

  def load(self):
    return self.pairs / self.capacity

  def check_resize(self):
    if self.load() > .7:
      self.resize()

  def hash(self, string):
    hashed = 5381
    byte_array = string.encode('utf-8')
    for byte in byte_array:
        hashed = ((hashed * 33) ^ byte) % 0x100000000
    return hashed % self.capacity
  
  def insert(self, key, value):
    index = self.hash(key)
    if self.storage[index]:
        new_pair = Pair(key, value)
        duplicate = False
        current_node = self.storage[index].head
        while current_node:
            if current_node.value.key == key:
                current_node.value = new_pair
                duplicate = True
                break
            else:
                current_node = current_node.next
        if not duplicate:
            self.storage[index].add_to_tail(new_pair)
            self.pairs += 1
            self.check_resize()
    else:
        new_pair = Pair(key, value)
        new_bucket = DoublyLinkedList()
        new_bucket.add_to_tail(new_pair)
        self.storage[index] = new_bucket
        self.pairs += 1
        self.check_resize()

  def remove(self, key):
    index = self.hash(key)
    if self.storage[index]:
      if self.storage[index].length == 1:
        if self.storage[index].head.value.key == key:
          self.storage[index] = None
        else:
          print("Warning: Key not found")
      else:
      # loop through, look for the key
        current_node = self.storage[index].head
        found_key = False
        while current_node:
          if current_node.value.key == key:
            self.storage[index].delete(current_node)
            found_key = True
            break
          else:
            current_node = current_node.next
        if not found_key:
          print("Warning: Key not found")
    else:
      print("Warning: Key not found")

  def retrieve(self, key):
    index = self.hash(key)
    if self.storage[index]:
      current_node = self.storage[index].head
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
        
  def resize(self):
    new_capacity = self.capacity * 2
    new_table = HashTable(new_capacity)
    for bucket in self.storage:
        if bucket:
            current_node = bucket.head
            while current_node:
                key = current_node.value.key
                value = current_node.value.value
                new_table.insert(key, value)
                current_node = current_node.next
        else:
            continue
    self.capacity = new_capacity
    self.storage = new_table.storage


def Testing():
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    print(ht.pairs, '<--- pairs')
    print(ht.load(), '<--- load')
    print(ht.capacity, '<--- capacity')
    ht.insert("line_2", "Filled beyond capacity")
    print(ht.pairs, '<--- pairs')
    print(ht.load(), '<--- load')
    print(ht.capacity, '<--- capacity')
    ht.insert("line_3", "Linked list saves the day!")
    print(ht.pairs, '<--- pairs')
    print(ht.load(), '<--- load')
    print(ht.capacity, '<--- capacity')
    ht.insert("line_4", "Automatic resizing")
    print(ht.pairs, '<--- pairs')
    print(ht.load(), '<--- load')
    print(ht.capacity, '<--- capacity')

    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # old_capacity = len(ht.storage)
    # ht = ht.resize()
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
