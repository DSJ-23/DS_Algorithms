a = "hello"
# print(len(a))


print(a[1:3])



def get_frequency(char, pattern):
    count = 0
    if pattern not in char:
        return 0
    else:
        while (len(char) >= len(pattern)):
            if char[0:len(pattern)] == pattern:
                count = count + 1
            char = char[1:len(char)]
            print(char)
    return count
            
print(get_frequency("bcdefbcbebc", " "))

 word = bool(re.match(r'\w.*', pattern))
    if word is False:
        return 0


def doSomething(blob, pattern):
    #Write your code here
    result = list(map(lambda x: get_frequency(x,pattern), blob))
    result.append(sum(result))
    result = list(map(lambda y: str(y), result))
    return "|".join(result)
    
def get_frequency(char, pattern):
    count = 0
    if pattern not in char:
        return 0
    else:
        while (len(char) >= len(pattern)):
            if char[0:len(pattern)] == pattern:
                count += 1
            char = char[1:len(char)]
    return count


  