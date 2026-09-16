"""
Problem:
1. Compute math result
2. Pay attention to order of operations - not really just operate and store
3. Truncate to 0 - int(a/b)
4. No invalid operations

Observations:
1. All operators operate on 2 inputs
2. no brackets

e.g 
5 + 3  -> 5 3 +

Sol 

1. iterate
2. Check Curr in list of operators
    - IF Operator: pop last 2 -> perform operation -> add result back to the stack
    - ELSE: add to stack
3. return top of stack

"""
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for token in tokens:
            if token in operators:
                a, b = int(stack.pop()), int(stack.pop())
                op_result = max(operators[token](a,b), 0)
                stack.append(op_result)
            else:
                stack.append(token)

        return stack.pop()