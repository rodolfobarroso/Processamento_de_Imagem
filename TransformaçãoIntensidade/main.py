from TransformIntensidade import TransformIntesidade

if __name__ == '__main__':
    print("Transformação de Intensidade:")
    intensidade  = TransformIntesidade('img/goku.png')
    intensidade.carregarImagem()
    op = -1
    menu = ' \n\nDigite 0 para sair\n'
    menu += '1 - Transformação para negativo\n'
    menu += '2  - Transformação Power Law\n'
    
    while op!= 0:
       # print(menu)
        op = input(menu)
        op = int(op)
        if op == 1:
            intensidade.negative()
        elif op == 2:
            print('Digite o valor do Gama e da constante')
            gama = float(input())
            c = float(input())
            intensidade.PowerLaw(gama,c) 
    
    print("Fim")
    



    

