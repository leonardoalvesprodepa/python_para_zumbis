peso = int(input('Insira o peso do peixe: '))
excesso = 0
multa = 0

if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso

print('Peso do peixe: %d Kg; Excesso: %d Kg; Multa: R$ %.2f.' %(peso, excesso, multa))
