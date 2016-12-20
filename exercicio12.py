# -*- coding: utf-8 -*-
n = 2
fatorial = 1
numero = int(input('Número: '))
while n <= numero:
    fatorial = fatorial * n
    n = n + 1
print 'fatorial (%d) = %d' % (numero, fatorial)
