import operator 

operations = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    }

n1, op, n2 = input ("gimme some math to do mate").split()

n1 = int(n1)
n2 = int(n2)

if op in operations:
    operation = operations[op]
    answer = operation(n1, n2)
    print(f"{n1} {op} {n2} = {answer}")
else: print(f"Invalid Operator: {op}")
