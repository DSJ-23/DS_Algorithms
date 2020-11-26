a = [1,1,2,2,2,3,3,4,4,4,6,6,6,6]
# b = list(dict.fromkeys(a))
# print(a.count(1))
# v = dict.fromkeys(a)
# print(b)
# print(v)

b = "kfjdkadsfj"
for i in b:
    print(i)
    
# print(Counter(a))
# eles = set()
# for i in a:
#     eles.add(i)

# print(eles)

def count_dict(list_number):
        values = dict.fromkeys(list_number)
        for i in list_number:
            values[i] = list_number.count(i)
        return values


def remove_dups(sorted_list):
    current= sorted_list[0]
    for i in sorted_list[1:]:
        if i == current:
            sorted_list.remove(i)
        else:
            current = i
    return sorted_list

# print(remove_dups(a))

def rem(array_sorted):
    for index, value in enumerate(array_sorted):
        print(index)
        if array_sorted[index] == array_sorted[index + 1]:
            array_sorted.pop(index)
    return array_sorted

# print(rem(a))


def remove_duplicates(sorted_array):
    for i in sorted_array:
        last = len(sorted_array) -1
        current = sorted_array.index(i)
        if current <= last:
            if i == sorted_array[current+1]:
                sorted_array.pop(current)
            break
        else:
            if i == sorted_array[current+1]:
                sorted_array.pop(current)
    return sorted_array 


# print(remove_duplicates(a))
# print(a.index(2))