ano = int(input('Digite o ano para saber se é bissexto: '))

if ano % 4 == 0 and ano % 100 != 0:
    print 'O ano de %d é bissexto' % ano
elif ano % 400 == 0:
    print 'O ano de %d é bissexto' % ano
else:
    print 'O ano de %d não é bissexto' % ano
