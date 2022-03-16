import unittest
from insertion_sort import insertion_sort
from merge_sort import merge_sort, merge

class TestSort(unittest.TestCase):
    a = [1,2,3,4,5,6,7]
    b = [7,6,5,4,3,2,1,0]
    c = [9,1,8,2,7,3,6,4,5]
    d = [1,2,3,0,7,8]
    error_message = 'Oh no no no no'

    def test_insertion(self):
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7], insertion_sort(self.a[:]), self.error_message)
        self.assertListEqual([0,1,2,3,4,5,6,7], insertion_sort(self.b[:]), self.error_message)
        self.assertListEqual([1,2,3,4,5,6,7,8,9], insertion_sort(self.c[:]), self.error_message)
        self.assertListEqual([0,1,2,3,7,8], insertion_sort(self.d[:]), self.error_message)

    def test_mergesort(self):
        self.assertListEqual([1,2,3,4,5,6,7], merge_sort(self.a[:], 0, len(self.a) - 1), self.error_message)
        self.assertListEqual([0,1,2,3,4,5,6,7], merge_sort(self.b[:], 0, len(self.b) - 1), self.error_message)
        self.assertListEqual([1,2,3,4,5,6,7,8,9], merge_sort(self.c[:], 0, len(self.c) - 1), self.error_message)
        self.assertListEqual([0,1,2,3,7,8], merge_sort(self.d[:], 0, len(self.d) - 1), self.error_message)

    def test_merge(self):
        # self.assertListEqual([1,2,3,4,5,6,7,8,9], merge([9,1,8,2,7,3,6,4,5], 0, 4, 8))
        # self.assertListEqual([1,2,3,4,5,6,7,8,9], [3, 6, 4, 5, 9, 1, 8, 2, 7])
        self.assertListEqual([1,2,3,4,5,6,7], merge(self.a[:], 0, (len(self.a) - 1) // 2, len(self.a)-1), self.error_message)
        # self.assertListEqual([0,1,2,3,4,5,6,7], merge(self.b[:], 0, (len(self.b) - 1) // 2, len(self.b)-1), self.error_message)
        self.assertListEqual([0,1,2,3,7,8], merge(self.d[:], 0, (len(self.d)-1) // 2, len(self.d)-1), self.error_message)


        
