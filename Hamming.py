class Hamming(object):

    def __init__(self,dados):
        self.dados = dados
        self.posic = []
        self.soma = []
        self.dados_errados = []
        self.paridades = []
    @property
    def converte_bin(self):
        
        binario = ''
        lista = []
        lista = [1,0,1,0,1,0,1,0]
        """
        for i in self.dados:
            binario += bin(ord(i))[2::] + ' ' #converte para binario e coloca os dados em uma lista

        for x in binario:
            if(x!=' '):
                lista.append(int(x))

        """
        self.dados = lista
        #print(self.dados)

    @property
    def coloca_paridade(self):
        lista = self.dados.copy()
        cont = 0
        for x in range(len(lista)):
            
            if(x == (2**cont)-1):
                self.dados.insert(x,"p") #coloca a paridade na lista de dados conforme as elevações de 2 inserindo o caractere "p" nos dados 
                self.posic.append(x+1)  
                cont+=1
                
        print(self.dados)
        #print("Posiçoes",self.posic) <- posições das paridades armazenadas em uma lista
                
    @property
    def verifica_paridade(self):
        lista = [[] for x in range(len(self.posic))] #matriz criada conforme a quantidade de paridades
        index = 0
        for i in range(len(self.posic)):
            if(i==0):
                for x in range(self.posic[i]-1,len(self.dados),i*2+2):
                    lista[i].append(x)      #adiciona as posições dos bits em uma matriz 
            else:
               ini = self.posic[i]-1     #caso o i seja diferente de 0
               cont=0
               
               while(ini<len(self.dados)):
                   lista[i].append(ini)    #armazena os indices dos bits que se relacionario com cada paridade
                   cont+=1
                   ini+=1
                   if(cont==self.posic[i]):
                       cont = 0
                       ini+=self.posic[i]

        for x in lista:
            x.pop(0)        #remove os indices das paridades pois eles não tem importância para a lista de indices de bits de dados
        
        for x in range(len(lista)):
            soma = 0
            for i in (lista[x]):
                if(self.dados[i]!='p'):   #insere os bits de paridade atraves das somas dos bits da cada linha da matriz,
                    soma+=self.dados[i]  #onde se a soma % 2 ==0 sera inserido 0 senao 1, no lugar do caractere "p" no indice na paridade na lista de dados
            if(soma%2==0):              #usando a lista de posições das paridades para saber onde o valor do bit de paridade será inserido
                self.dados.remove('p')
                self.dados.insert(self.posic[x]-1,0)
            else:
                self.dados.remove('p')
                self.dados.insert(self.posic[x]-1,1)
            self.soma.append(soma) #coloca o resultado das somas dos bits relacionados a cada paridade em uma lista pois 
        self.paridades = lista     #logo era será necessário


        
        #print("Lista das paridades",self.paridades) 
        #print("Os dados",self.dados)
        #print("As somas",self.soma)
        
    @property
    def gera_erro(self):
        lista = self.dados.copy()  #copia da lista de dados 
        for x in range(2,4):
            if(self.dados[self.posic[x]-1] == 0):  #modifica as paridades p3 e p4 invertendo seus valores com base em condições
                self.dados[self.posic[x]-1] = 1
            else:
                self.dados[self.posic[x]-1] = 0
        self.dados_errados = self.dados.copy() #nova lista com dados errados
        print("Os dados sem erro",lista)
        print("Os dados com erro",self.dados)

        self.dados = lista #lista de dados originais 

    @property
    def corrige_erro(self):
        errados = []
        cont = 0
        for x in range(len(self.posic)):
            if(self.dados_errados[self.posic[x]-1]== 1 and (self.soma[x] % 2 == 0)):
               errados.append(cont)
            if(self.dados_errados[self.posic[x]-1]== 0 and (self.soma[x] % 2 == 1)): #compara os valores de soma de cada bit de paridade
               errados.append(cont)                                                  #caso seja detectado erro as posiçoes das paridades com erro serão armazenadas
            cont+=1
            
        print("Indices com as paridades erradas",errados)
        conjuntos = []   

        for x in errados:
            for i in self.paridades[x]:
                conjuntos.append(i) # a lista conjuntos armazena os indices dos valores relacionados as paridades erradas que foram encontradas
                                    # exemplo p1 = [1,3,5], p2 = [2,3,6,7], cojuntos = [1,3,5,2,3,6,7]
        errados.clear()#a lista é limpa para ser reusada
        for x in conjuntos:
            if(conjuntos.count(x)>=2):  #conta cada elemento da lista e busca sempre o elemento em comum entre essas paridades 
                if(x not in errados):   # no exemplo a cima o bit em comum entre as paridades está na posição 7 pois ele se repete duas vezes na lista conjuntos
                    errados.append(x)   # apos isso esse indice é armazenado 

        for x in errados:
            if(self.dados_errados[x]==1):
                self.dados_errados[x] = 0 # aqui ocorre somente a inversão dos dados errados
            else:
                self.dados_errados[x] = 1
            
            
        
        
       
                
                    
        
        
        #print("Dados errados corrigidos",self.dados_errados)
        #print("Os conjuntos",conjuntos)
        #print("Bits em comum",errados)

        for x in range(len(self.posic)-1,-1,-1):
            self.dados_errados.pop(self.posic[x]-1) #remoção dos bits de paridade


        print("O dados corrigidos",self.dados_errados) #dados corrigidos
        
        
         
               
        
                
                       
                   
               
                   
                   
                    
                
                    
                
                
                
        
op = 1
while op!=0:
    print("Digite 0 para encerrar o programa")
    print("Digite 1 para digitar a frase")
    print("Digite 2 para ver os dados convertidos com as paridades inseridas")
    print("Digite 3 para gerar um erro")
    print("Digite 4 para corrigir o erro")
    op = int(input(""))
    if(op==1):
        frase = str(input("Digite a frase para ser convertida\n"))
        hamming = Hamming(frase)
    if(op==2):
        hamming.converte_bin
        hamming.coloca_paridade
        hamming.verifica_paridade
    if(op==3):
        print("ERRO GERADO COM SUCESSO\n")
        hamming.gera_erro
    if(op==4):
        print("ERRO CORRIGIDO COM SUCESSO\n")
        hamming.corrige_erro
        






