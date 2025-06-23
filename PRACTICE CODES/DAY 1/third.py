#string manipulation
a = "\tpythoN"
b=89
print(a.title())
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.center(4))
print(a.startswith("p"))
print(a.expandtabs(2))
print(a.find("y"))
print(a.isnumeric())
print(b.is_integer())


a = ' '
b=('a','b','c')
print(a.join(b))