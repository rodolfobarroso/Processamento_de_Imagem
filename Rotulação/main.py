from Rotulacao import Rotulacao

if __name__ == '__main__':
	print("Rotulação:")

	rotulacao = Rotulacao("img/formas.png")
	rotulacao.carregarImagem()
	op = -1

	menuStr = "\n\nDigite 0 para sair\n"
	menuStr += "Rotulação\n1 - Rotular\n"

	while op != 0:
		op = input(menuStr)
		op = int(op)
		if op == 1:
			rotulacao.executar()
			
	print("Fim")
