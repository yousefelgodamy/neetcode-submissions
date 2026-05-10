class MyHashSet:

    def __init__(self):
        self.table_size = 1_000
        self.hash_table = [[]] * self.table_size

    def add(self, key: int) -> None:
        if key not in self.hash_table[key // self.table_size]:
            self.hash_table[key // self.table_size].append(key)

    def remove(self, key: int) -> None:
        internal_list = self.hash_table[key // self.table_size]
        try:
            internal_list.remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        internal_list = self.hash_table[key // self.table_size]
        return key in internal_list

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)