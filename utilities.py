s = "anagram"


def remove_char(str, n):
    first = str[0:n]
    second = str[n+1:]
    return first + second

def find_index(s, ind):
    found_index = -1
    try:
        found_index = s.index(ind)
    except:
        pass
    return found_index


print(find_index(s, "z"))







