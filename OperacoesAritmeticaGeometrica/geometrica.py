import numpy as np
from PIL import Image
import math


def reflexao (mat , m , n ,eixo):
    x = lambda x : x
    y = lambda y : y
    saida = np.zeros([m,n])
    if eixo == 1 :
        x = lambda x: m -1 -x
    else:
        y = lambda y: n-1 -y 
    for i in range(m):
        for j in range(n):
            saida[i,j] = mat[x(i),y(j)]
    img  = Image.fromarray(saida)
    Image._show(img)


if __name__ == '__main__':
    img  = Image.open('img/ovo.jpg')
    #Image._show(img)
    img  = img.convert('L')
    matriz = np.asarray(img)
    while(True):
        print("0: sair")
        print("1: reflexao no eixo x")
        print("2: reflexao no eixo y")
        eixo = input()
        if eixo =='0':
            break
        else:  
            m,n = matriz.shape
            print("m: {} n: {}".format(m , n))
            #rotacao(matriz,m,n,int(eixo))
            reflexao(matriz,m,n,int(eixo))
    print("Fim")