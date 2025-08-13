import MYTOOLS as mt
n1=int(input("Digite o número de casas decimais desejada para pi: "))
n2=int(input("Digite o número de casas decimais desejada para e: "))
pi=mt.pi_real(n1)
e=mt.e_real(n2)
print("pi = "+pi)
print("e = "+e)
