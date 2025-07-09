def decryptCiphertext(d,c,N):
    flag = pow(c,d,N)
    return flag

N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932
d = "A certain pair of parameters for a certain number from our man Euler may come in handy. See previous challenge for yourself"
print(decryptCiphertext(d,c,N))
