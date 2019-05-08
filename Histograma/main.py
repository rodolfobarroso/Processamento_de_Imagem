from Histograma import Histograma

if __name__ == '__main__':
	print("Histograma:")

	histograma = Histograma("img/carro.jpg")
	histograma.carregarImagem()

	histograma.executar()
			
	print("Fim execução!!")
