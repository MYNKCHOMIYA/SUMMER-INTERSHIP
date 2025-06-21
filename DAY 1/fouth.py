l ="typon"
e = "12345"
str = "this is python!!!"
encoding =str.maketrans(l,e)
print(encoding)
print(str.translate(encoding))