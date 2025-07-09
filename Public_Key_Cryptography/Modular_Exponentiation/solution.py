def inverseOp(b,e,m):
    flag = pow(b,e,m)
    return flag

# c = b^e mod m
b = 101
e = 17
m = 22663
print(inverseOp(101,17,22663))
