from readerwriterlock import rwlock
from hipster.min_heap import MinHeap
from hipster.max_heap import MaxHeap
from contradict.hashmap import Hashmap


class SortedDict(Hashmap):
    def __init__(self):
        super().__init__()
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()
        lock = rwlock.RWLockFair()
        self.read_lock = lock.gen_rlock()
        self.write_lock = lock.gen_wlock()
        self.dict = {}

    def get(self, key):
        with self.read_lock:
            if key in self.dict:
                return self.dict[key]
            return None

    def set(self, key, value):
        with self.write_lock:
            self.dict[key] = value
            self.min_heap.push(key)
            self.max_heap.push(key)

    def contains(self, key):
        with self.read_lock:
            return key in self.dict

    def items(self, reverse=False):
        res = []
        temp = []
        with self.write_lock:
            if reverse:
                while len(self.max_heap) > 0:
                    curr = self.max_heap.pop()
                    res.append((curr, self.dict[curr]))
                    temp.append(curr)
                for t in temp:
                    self.max_heap.push(t)
            else:
                while len(self.min_heap) > 0:
                    curr = self.min_heap.pop()
                    res.append((curr, self.dict[curr]))
                    temp.append(curr)
                for t in temp:
                    self.min_heap.push(t)
        return res

    def keys(self, reverse=False):
        res = []
        temp = []
        with self.write_lock:
            if reverse:
                while len(self.max_heap) > 0:
                    curr = self.max_heap.pop()
                    res.append(curr)
                    temp.append(curr)
                for t in temp:
                    self.max_heap.push(t)
            else:
                while len(self.min_heap) > 0:
                    curr = self.min_heap.pop()
                    res.append(curr,)
                    temp.append(curr)
                for t in temp:
                    self.min_heap.push(t)
        return res

    def values(self, reverse=False):
        res = []
        temp = []
        with self.write_lock:
            if reverse:
                while len(self.max_heap) > 0:
                    curr = self.max_heap.pop()
                    res.append(self.dict[curr])
                    temp.append(curr)
                for t in temp:
                    self.max_heap.push(t)
            else:
                while len(self.min_heap) > 0:
                    curr = self.min_heap.pop()
                    res.append(self.dict[curr])
                    temp.append(curr)
                for t in temp:
                    self.min_heap.push(t)
        return res


