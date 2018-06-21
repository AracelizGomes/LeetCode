'''Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
'''
class ListStack:
    def __init__(self):
        self._L = []
        
    def push(self, item):
        self._L.append(item)

    def pop(self):
        return self._L.pop()

    def peek(self):
        return self._L[-1]

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self) == 0

class Solution(object):
    def evalRPN(self, tokens):
        stack = ListStack()
        ops = {
          "+": (lambda a, b: b+a),
          "*": (lambda a, b: b*a), 
          "/": (lambda a, b: b/a), 
          "-": (lambda a, b: b-a)
        }
        for i in tokens.split(" "):
          if i in ops:
            n1 = stack.pop()
            n2 = stack.pop()
            result = ops[i](n1, n2)
            stack.push(result)
          else:
            stack.push(float(i))
        
        return stack.pop()

p1 = Solution()
print(p1.evalRPN("1 2 +"))
            
