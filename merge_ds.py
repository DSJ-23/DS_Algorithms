aa = [0, 57, 59, 90]
bb = [6, 17, 20, 60, 63, 74, 95, 97]

def merge(num1, num2):
    first = 0

    if num1 is None:
        return num2
    if num2 is None:
        return num1

    while len(num2) > 0:
        if first == len(num1):
            for i in num2:
                num1.insert(first, i)
                first += first
            break
        elif num2[0] > num1[first]:
            first = first + 1
        elif num2[0] <= num1[first]:
            num1.insert(first, num2.pop(0))
    return num1

aa = bb
print(aa)