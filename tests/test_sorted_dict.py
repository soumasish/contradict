import unittest
from contradict.sorted_dict import SortedDict


class TestSortedDict(unittest.TestCase):
    def test_get_set(self):
        sorted_dict = SortedDict()
        sorted_dict.set('A', 12)
        sorted_dict.set('B', 13)
        sorted_dict.set('C', 15)
        self.assertEqual(sorted_dict.get('B'), 13)

    def test_items(self):
        sorted_dict = SortedDict()
        sorted_dict.set('A', 12)
        sorted_dict.set('B', 13)
        sorted_dict.set('C', 15)
        res = []
        for k, v in sorted_dict.items():
            res.append((k, v))
        self.assertEqual(res[0], ('A', 12))

    def test_keys(self):
        sorted_dict = SortedDict()
        sorted_dict.set('A', 12)
        sorted_dict.set('B', 13)
        sorted_dict.set('C', 15)
        res = []
        for k in sorted_dict.keys():
            res.append(k)
        self.assertEqual(res[0], 'A')

    def test_values(self):
        sorted_dict = SortedDict()
        sorted_dict.set('A', 12)
        sorted_dict.set('B', 13)
        sorted_dict.set('C', 15)
        res = []
        for v in sorted_dict.values():
            res.append(v)
        self.assertEqual(res[0], 12)

    def test_items_reverse(self):
        sorted_dict = SortedDict()
        sorted_dict.set('A', 12)
        sorted_dict.set('B', 13)
        sorted_dict.set('C', 15)
        res = []
        for k, v in sorted_dict.items(reverse=True):
            res.append((k, v))
        self.assertEqual(res[0], ('C', 15))

    def test_keys_reverse(self):
        sorted_dict = SortedDict()
        sorted_dict.set('A', 12)
        sorted_dict.set('B', 13)
        sorted_dict.set('C', 15)
        res = []
        for k in sorted_dict.keys(reverse=True):
            res.append(k)
        self.assertEqual(res[0], 'C')

    def test_values_reverse(self):
        sorted_dict = SortedDict()
        sorted_dict.set('A', 12)
        sorted_dict.set('B', 13)
        sorted_dict.set('C', 15)
        res = []
        for v in sorted_dict.values(reverse=True):
            res.append(v)
        self.assertEqual(res[0], 15)



