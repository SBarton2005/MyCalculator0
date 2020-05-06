def add(a):
  #This is addition
  c = 0
  for b in a:
    c += b
  return c
def sub(a, b):
  #This is subtraction
  return a - b
def mul(a):
  #This is multiplication
  c = 1
  for b in a:
    c = c * b
  return c
def div(a, b):
  #This is division
  return a / b
def rem(a, b):
  #This is finding the remainder
  return a % b
def exp(a, b):
  #This is exponentials
  return a ** b
def roo(a, b):
  #This is rooting
  return a ** (1 / b)
def fac(a):
  #This is factorials
  i = 1
  while a > 0:
    i = i * a
    a -= 1
  return i
def cal(o, a, b = 0):
  if o == "add":
    return add(a)
  elif o == "sub":
    return sub(a, b)
  elif o == "mul":
    return mul(a)
  elif o == "div":
    return div(a, b)
  elif o == "rem":
    return rem(a, b)
  elif o == "exp":
    return exp(a, b)
  elif o == "roo":
    return roo(a, b)
  elif o == "fac":
    return fac(a)
  else:
    return "You didn't give an opperation we have"