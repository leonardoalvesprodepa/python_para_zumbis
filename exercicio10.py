# -*- coding: utf-8 -*-
n = 1
soma = 0

while n <= 10:
    x = int(input('Digite o %d:' % n))
    soma = soma + x
    n = n + 1
print 'Média é', soma /( n - 1)
