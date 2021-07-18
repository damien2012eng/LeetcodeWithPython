def validParentess(array):
    left =  ['(','[','{']
    right = [')',']','}']
    stack = []
    for elem in array:
        if elem in left:
            stack.append(elem)
        elif elem in right:
            # if the current element in the array does not match with the top of stack
            # or stack is empty while the current element is right. Return False
            if not stack or right.index(elem) != left.index(stack[-1]):
                return False
            else:
                stack.pop()
        print(stack)
    
    # if the array has been run out, stack is not empty. Return False
    if stack:
        return False
    else:
        return True


array = ['(','[','{',')','}',']']
print(validParentess(array))

