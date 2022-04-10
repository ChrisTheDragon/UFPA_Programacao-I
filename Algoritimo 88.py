# -------------------------------------------------
# --------------  Algoritmo 88  -------------------
# -------------------------------------------------
print(f'=-' * 25)
print(f'CALCULADORA'.center(45))
print(f'-=' * 25)
print(f'Digite:\n'
      f'[ + ] para soma\n'
      f'[ - ] para subtração\n'
      f'[ * ] para multiplicação\n'
      f'[ / ] para divisão\n'
      f'[ S ] para sair')
while True:
      op = str(input(f'-> ')).strip().lower()[0]
      n1 = int(input('Digite o primeiro valor: '))
      n2 = int(input('Digite o segundo valor: '))

      if op == '+':
            print(f'{n1} + {n2} = {n1 + n2}')
      elif op == '-':
            print(f'{n1} - {n2} = {n1 - n2}')
      elif op == '*':
            print(f'{n1} * {n2} = {n1 * n2}')
      elif op == '/':
            print(f'{n1} / {n2} = {n1 / n2}')
      elif op == 's':
            break
      else:
            print(f'Opção inválida! Digite novamente')