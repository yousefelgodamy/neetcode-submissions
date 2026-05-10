class MyHashMap:

    def __init__(self):
        self.map_size = 1_000
        self.hash_map = [[]] * self.map_size

    def put(self, key: int, value: int) -> None:
        internal_list = self._lookup(key)
        for item_pair in internal_list:
            if key == item_pair[0]:
                item_pair[1] = value
                return
        
        internal_list.append([key, value])

    def get(self, key: int) -> int:
        internal_list = self._lookup(key)
        for item_pair in internal_list:
            if item_pair[0] == key:
                return item_pair[1]
        return -1

    def remove(self, key: int) -> None:
        internal_list = self._lookup(key)
        for i in range(len(internal_list)):
            if internal_list[i][0] == key:
                internal_list.pop(i)
                break

    
    def _lookup(self, key: int) -> List:
        return self.hash_map[key % self.map_size]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)