def reverse(stack):
    #this function can't be iterative because the size of the stack stays constant (no termination condition for loop)
    if not stack:
        return
    temp = stack.pop()
    reverse(stack)
    insert_at_bottom(stack, temp)
    return stack 

def insert_at_bottom(stack, el):
    if not stack:
        stack.append(el)
        return
    temp = stack.pop()
    insert_at_bottom(stack, el)
    stack.append(temp)


# print(reverse([1, 2, 4]))
print(reverse([1, 2, 4]))