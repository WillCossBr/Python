#----------------------------------------------------------------

#def contar(num=11, caractere='+'):
#    for i in range (1, num):
#        print(caractere)
#
#if __name__=='__main__':
#    contar(8, '&')

#----------------------------------------------------------------

x = 5
y = 6
z = 3

def soma_mult(a,b,c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c

if __name__=='__main__':
    res = soma_mult(x, y)
    print(res)

#----------------------------------------------------------------