import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
    '%' : operator.mod,
    '^' : operator.xor,
}
def basic_op(oper, value1, value2):
  value1, value2 = int(value1), int(value2)
  return ops[oper](value1, value2)

print(basic_op('+', 4, 7))
print(basic_op('-', 15, 18))
print(basic_op('*', 5, 5))
print(basic_op('/', 49, 7))