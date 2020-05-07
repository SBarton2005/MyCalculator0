def add(a):
  #This is addition
  c = 0
  for b in a:
    b = int(b)
    c += b
  return c
def sub(a, b):
  #This is subtraction
  return a - b
def mul(a):
  #This is multiplication
  c = 1
  for b in a:
    b = int(b)
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
def pll(a, b):
  #Find the hypotenuse
  c = a ** 2
  d = b ** 2
  e = c + d
  f = e ** .5
  return f
def phl(a, b):
  #Find the missing leg
  c = a ** 2
  d = b ** 2
  e = c - d
  f = e ** .5
  return f
def qua(a, b, c):
  #Solve quadratic formula
  d = b ** 2
  e = 4 * a * c 
  f = d - e
  g = f ** .5
  ha = - b + g
  hb = - b - g
  ia = ha / 2 / a
  ib = hb / 2 / a
  return ia, ib
def irt(a, b, c):
  #Is it a right triangle
  d = a ** 2
  e = b ** 2
  f = c ** 2
  if d + e == f:
    return True
  else:
    return False
def cal(o, a, b = 0, c = 0):
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
  elif o == "pll":
    return pll(a, b)
  elif o == "phl":
    return phl(a, b)
  elif o == "qua":
    return qua(a, b, c)
  elif o == "irt":
    return irt(a, b, c)
  else:
    return "You didn't give an opperation we have"
o = input("Opperation: ")
if o == "add" or o == "mul":
  q = input("a: ")
  a = q.split(" ")  
else:
  a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print(cal(o, a, b, c))