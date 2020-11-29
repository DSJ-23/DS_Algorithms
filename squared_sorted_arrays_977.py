class Solution:

    def sorted_squared(self, A):
        sorted_squares = []
        index_first = 0
        index_last = len(A) -1
        while index_first != index_last:
            first = abs(A[index_first])
            last = abs(A[index_last])
            if first >= last:
                sorted_squares.insert(0, first**2)
                index_first += 1
            else:
                sorted_squares.insert(0, last**2)
                index_last = index_last -1
        sorted_squares.insert(0, A[index_first]**2)
        return sorted_squares

    def SortedSquared(self, A):
        sorted_squares = []
        index_first = 0
        index_last = len(A) -1
        while index_first != index_last:
            first = A[index_first]
            last = A[index_last]
            if first > last:
                sorted_squares.insert(1, first**2)
                sorted_squares.insert(0, last**2)
            else:
                sorted_squares.insert(0, first**2)
                sorted_squares.insert(1, last**2)
            index_last -= 1
            index_first += 1
        return sorted_squares


bb = [-5,-4,-1,0,3,10,11]

eg = [-4,-1,0,3,10]

par = [-4,-1,3, 10]

a = Solution()
# print(a.SortedSquared(eg))
# print(a.sorted_squared(bb))
# print(a.sorted_squared(par))