def eulerTotient(p,q):
    phi = (p-1)*(q-1)
    return phi

def modMultiplicativeInv(e,totient):
    flag = pow(e,-1,totient)
    return flag

# private key d = e^-1 mod phi(m) -> d = e^-1 mod ((p-1)(q-1))
e = 65537
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
print(modMultiplicativeInv(e,eulerTotient(p,q)))
