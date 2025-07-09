def rsaEncrypt(b,e,p,q):
   flag = pow(b,e,p*q)
   return flag

# RSA - N = p*q, c = b^e mod N
b = 12
e = 65537
p = 17
q = 23
print(rsaEncrypt(b,e,p,q))
