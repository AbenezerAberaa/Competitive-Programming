class MyHashMap:

    def __init__(self):
        self.my_map = {}

    def put(self, key: int, value: int) -> None:
        self.my_map[key]=value

    def get(self, key: int) -> int:
        if key in self.my_map:
            return self.my_map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.my_map:
            self.my_map.pop(key)
