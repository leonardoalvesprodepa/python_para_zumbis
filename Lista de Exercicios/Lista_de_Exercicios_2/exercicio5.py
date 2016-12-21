# -*- coding:utf-8 -*-
a = int(input("Insira o primeiro: "))
b = int(input("Insira o segunto: "))
c = int(input("Insira o terceiro: "))

if a > b and a > c:
    print 'O primeiro é maior'
elif b > a and b > c:
    print 'O segundo é maior'
elif c > a and c > b:
    print 'O terceiro é maior'
else:
    print 'Existêm valores iguais'


if a < b and a < c:
    print 'O primeiro é menor'
elif b < a and b < c:
    print 'O segundo é menor'
elif c < a and c < b:
    print 'O terceiro é menor'
else:
    print 'Existêm valores menor'
