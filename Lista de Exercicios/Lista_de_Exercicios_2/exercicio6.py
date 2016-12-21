# -*- coding:utf-8 -*-
valor_hora = int(input("Insira o valor da sua hora: "))
horas_mes = int(input("Insira quantas horas trabalha por mês: "))

salario_bruto = valor_hora * horas_mes
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato   

print '+ Salário Bruto : R$', salario_bruto 
print '-IR : R$', ir 
print '-INSS : R$', inss
print '-Sindicato : R$', sindicato 
print '= Salário liquido : R$', salario_liquido
