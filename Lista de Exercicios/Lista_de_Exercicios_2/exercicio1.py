# -*- coding:utf-8 -*-
a = int(input("Insira o primeiro lado do triângulo: "))
b = int(input("Insira o segunto lado do triângulo: "))
c = int(input("Insira o terceiro lado do triângulo: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print ('Os lados formam um triângulo')
    if a == b and b == c:
        print 'Triângulo Equilátero'

    elif a == b or a == c or b == c:
        print 'Triângulo Isósceles'

    else:
        print 'Triângulo Escaleno'

else:
    print 'Os lados informados não formam um triângulo'
