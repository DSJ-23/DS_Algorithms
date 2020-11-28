class Stack():
    def __init__(self):
        self.data = []

    def get_stack(self):
        return self.data

    def pop(self):
        return self.data.pop()

    def add(self, item):
        self.data.append(item)

    def get(self):
        return self.data[-1]

    def is_empty(self):
        return self.data == []

    def remove(self, item):
        self.data.remove(item)
        
    
def count_dict(list_number):
        values = dict.fromkeys(list_number)
        for i in list_number:
            values[i] = list_number.count(i)
        return values



#contain duplicates 2
# 448 find all numbers disappeared in array
