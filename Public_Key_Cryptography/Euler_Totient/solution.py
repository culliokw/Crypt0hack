def eulerTotient(p,q):
    flag = (p-1)*(q-1)
    return flag

# Euler's Totient of N given N=p*q and p,q are prime - N=(p-1)(q-1)
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
print(eulerTotient(p,q))
