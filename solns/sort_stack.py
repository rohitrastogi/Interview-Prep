def sort_stack(s):
    if not s:
        return s

    second = []
    second.append(s.pop())

    while s:
        temp = s.pop()
        while second and second[-1] < temp:
            s.append(second.pop())
        second.append(temp)

    return second

stack = [1, 5, 3, 4]
print(sort_stack(stack))