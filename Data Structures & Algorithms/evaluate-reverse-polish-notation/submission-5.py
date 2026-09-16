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
            "/": lambda a,b: int(operator.truediv(a,b)),
        }

        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()

                op_result = operators[token](left,right)
                stack.append(op_result)
            else:
                stack.append(int(token))

        return stack.pop()










