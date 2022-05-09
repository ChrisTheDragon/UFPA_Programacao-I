from random import randint

tent = 1
op = 'S'

print('VAMOS JOGAR UM JOGO!\nJogo Advinha o Numero:')
while op == 'S':
	dific = int(input('Entre com a Dificuldade: [1 | 2 | 3]: '))
	if dific == 1:
		comNum = randint(0, 10)
		jogNum = int(input('Escolhi um numero entre 0 e 10\nQue numero voce acha que é?: '))
		tent = 1
		while comNum != jogNum:
			if jogNum < comNum:
				jogNum = int(input('Mais! Tente Novamente '))
				tent += 1
			if jogNum > comNum:
				jogNum = int(input('Menos! Tente Novamente '))
				tent += 1
		print(f'PARABENS! Voce Acertou!\nE só levou {tent} jogadas para isso!')
		if tent < 2:
			print('Voce leu minha mente!')
		elif tent >= 2 and tent <= 4:
			print('Bem impressionante!')
		elif tent >= 5 and tent <=  6:
			print('Tenta mais na proxima fera!')
		elif tent > 7:
			print('Vai te benzer pra ve se da mais sorte!')
		
		op = str(input('Jogar Novamente? ')).upper()[0]
		
	elif dific == 2:
		comNum = randint(0, 100)
		jogNum = int(input('Escolhi um numero entre 0 e 100\nQue numero voce acha que é?: '))
		tent = 1
		while comNum != jogNum:
			if jogNum < comNum:
				jogNum = int(input('Mais! Tente Novamente '))
				tent += 1
			if jogNum > comNum:
				jogNum = int(input('Menos! Tente Novamente '))
				tent += 1
		print(f'PARABENS! Voce Acertou!\nE só levou {tent} jogadas para isso!')
		if tent < 2:
			print('Voce leu minha mente!')
		elif tent >= 2 and tent <= 4:
			print('Bem impressionante!')
		elif tent >= 5 and tent <=  6:
			print('Tenta mais na proxima fera!')
		elif tent > 7:
			print('Vai te benzer pra ve se da mais sorte!')
		
		op = str(input('Jogar Novamente? ')).upper()[0]

	elif dific == 3:
			comNum = randint(0, 1000)
			jogNum = int(input('Escolhi um numero entre 0 e 1000\nQue numero voce acha que é?: '))
			tent = 1
			while comNum != jogNum:
				if jogNum < comNum:
					jogNum = int(input('Mais! Tente Novamente '))
					tent += 1
				if jogNum > comNum:
					jogNum = int(input('Menos! Tente Novamente '))
					tent += 1
			print(f'PARABENS! Voce Acertou!\nE só levou {tent} jogadas para isso!')
			if tent < 2:
				print('Voce leu minha mente!')
			elif tent >= 2 and tent <= 4:
				print('Bem impressionante!')
			elif tent >= 5 and tent <=  6:
				print('Tenta mais na proxima fera!')
			elif tent > 7:
				print('Vai te benzer pra ve se da mais sorte!')
			op = str(input('Jogar Novamente? ')).upper()[0]
	else:
		print('Opção Inválida!')
		dific = int(input('Entre com a Dificuldade: [1 | 2 | 3]: '))
print('PROGRAMA FINALIZADO!')