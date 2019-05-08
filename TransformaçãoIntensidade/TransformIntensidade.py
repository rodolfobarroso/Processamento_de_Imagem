import numpy as np 
from PIL import Image


class TransformIntesidade():

    def __init__(self,nome_image):
        self.nome_image = nome_image
        self.m = 0
        self.n = 0
        self.matriz = []
        self.img = []
    
    def carregarImagem(self):
        img = Image.open(self.nome_image)
        self.img = img.convert('L')
        self.matriz = np.asarray(self.img)
        self.m, self.n = self.matriz.shape
        print("linhas: {} e colunas: {}".format(self.m,self.n))
        print(self.matriz)

    def negative(self):
        L = 255
        saida  = np.zeros([self.m , self.n])
        m1, n1 = saida.shape
        print('linhas : {} coluna: {}'.format(m1,n1))

        for i in range(self.m):
            for j in range(self.n):
                saida[i,j] = L  - self.matriz[i,j]

        img  = Image.fromarray(saida)
        Image._show(img)

    def PowerLaw(self,gama,c=1):
        saida = np.zeros([self.m,self.n])
        for i in range(self.m):
            for j in range(self.n):
                saida[i,j] = int(c*(self.matriz[i,j]**gama))

        img = Image.fromarray(saida)
        Image._show(img)

