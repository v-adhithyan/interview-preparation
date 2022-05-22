'''
Quick sort algo:
https://www.youtube.com/watch?v=7h1s2SojIRw

Partition algorithm
while i < j
    - At first choose the first element as pivot
    - Set i=low, j=high
    - increment i while array[i] <= pivot
    - increment j while array[j > pivot
    - if i < j, swap array[i], array[j]
    - return j which will be pivot element

Quicksort algo
while low < high
    - partition the array
    - call partition from low to pivot
    - call partition from pivot + 1 to high
'''
from math import inf as infinity


class Sort:

    def __init__(self, array):
        self.array = array
        self.array.append(infinity)

    def partition(self, low, high):
        i = low
        j = high
        pivot = self.array[low]

        while i < j:
            while self.array[i] <= pivot:
                i += 1
            while self.array[j] > pivot:
                j -= 1
            if i < j:
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[low], self.array[j] = self.array[j], self.array[low]
        return j

    def quick_sort(self, low, high):
        if low < high:
            partition_index = self.partition(low, high)
            self.quick_sort(low, partition_index)
            self.quick_sort(partition_index + 1, high)

    def sort(self):
        low = 0
        high = len(self.array) - 1
        self.quick_sort(low, high)


if __name__ == '__main__':
    a = [6, 5, 8, 9, 3, 10, 15, 12, 16]
    s = Sort(a)
    s.sort()
    print(s.array)

    a = [16, 12, 6, 8, 10, 9, 5, 15, 3]
    s = Sort(a)
    s.sort()
    print(s.array)
