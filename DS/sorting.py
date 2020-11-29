class Sorting:

    def bubble_sort(self, data):
        sorted_index = self.isSortedReturnIndex(data)
        if sorted_index is True:
            return data
        else:
            swap_nodes = self.swap_list(sorted_index, sorted_index + 1, data)
            return self.bubble_sort(swap_nodes)

    def swap_list(self, first_index, second_index, data):
        size = len(data) 
        if first_index < size and second_index < size:
            data[first_index], data[second_index] = data[second_index], data[first_index]
        else:
            return False
        return data

    def isSorted(self, data):
        for index, value in enumerate(data[:-1]):
            last_element_index =  len(data) 
            if value > data[index + 1]:
                return False
        return True

    def isSortedReturnIndex(self,data):
        for index, value in enumerate(data[:-1]):
            last_element_index =  len(data) 
            if value > data[index + 1]:
                return index
        return True



a = Sorting()

# bb = [1,2,3,4,5,6,7]

# bbc = [33,2,1,4,45,3,2]
# aa = [1,2,5,6,7,88, 9]
# a1 = [2,2,2,2,2,2,2]
# test1 = [1,33,344,2342,23423423342]

# print(a.isSorted(bb))
# print(a.isSorted(bbc))
# print(a.isSortedReturnIndex(bbc))
# print(a.isSorted(a1))
# print(a.isSorted(test1))

