#Evaluate Reverse Polish Notation
#Logic:
#values in stack represent computation that hasn't been evaluated
#pop values off the stack once we've seen an operator 
#if there arent two values in the stack before we've seen an operator, we dont havea valid RPN string
#if after evaluating the string, there is more than one value left in the stack, we have an invalid RPN string 

def evaluate(tokens):
    stack = []
    operators = set(['+', '-', '*', '/'])
    for token in tokens:
        if token not in operators:
            stack.append(token)
        else:
            if len(stack) < 2:
                raise Exception('There must be at least 2 operands to execute an operation!')
            val1 = int(stack.pop(len(stack) - 1))
            val2 = int(stack.pop(len(stack) - 1))
            stack.append(compute(val1, val2, token))
    if len(stack) > 1:
        raise Exception('Missing an operand!')
    return int(stack[0])

def compute(val1, val2, op):
    if op == '-':
        return val2 - val1
    elif op == '+':
        return val2 + val1
    elif op == '/':
        return round(val2/val1, 0)
    else:
        return val2*val1

print(evaluate(['2', '1', '+', '3', '*']))
print(evaluate(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
#print(evaluate(['5', '10']))
print(evaluate(['10', '/', '2']))

