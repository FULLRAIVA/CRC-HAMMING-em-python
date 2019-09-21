from random import randint
class crc(object):
    def __init__(self,dados,polinomio):
        self.poli = polinomio
        self.dados = dados
        self.gerador = None
        self.crc = None
        self.index = []
    @property
    def calcula_polinomio(self):
        lista = []
        for x in range(len(self.poli)):
            if(self.poli[x]=="^"):
                lista.append(int(self.poli[x+1]))
            elif((self.poli[x]=="x") and (self.poli[x+1]!="^")):
                 lista.append(1)
            elif(self.poli[x] == "1"):
                lista.append(0)
        #print("A lista",lista)
        lista2 = [0 for x in range(max(lista)+1)]
        for x in lista:
            lista2[x] = 1
        lista2 = lista2[::-1]
        
        self.gerador = lista2.copy()
        #print("O gerador",self.gerador)
        lista2.clear()
        for x in self.dados:
            lista2.append(int(x))
        self.dados = lista2
        
        
        for x in range(max(lista)):
            self.dados.append(0)
            self.index.append(len(self.dados)-1)
        #print("Os dados",self.dados)
        #print("INdex ",self.index)

        

    @property
    def calcula_crc(self):
        lista = []
        cont = 0
        conf = False
        
        while(cont!=len(self.dados)):
            if(not conf):
                if(self.dados[cont] == 1):
                    for i in range(len(self.gerador)):
                        lista.append(self.dados[i] ^ self.gerador[i])
                else:
                    for i in range(len(self.gerador)):
                        lista.append(self.dados[i] ^ 0)
                lista.pop(0)
                lista.append(self.dados[i]+1)
                conf = True
                cont += len(self.gerador) +1
                
                #print("the cont",cont)
                #print("A lista",lista)
                
            else:
                if(lista[0] == 1):
                    for i in range(len(self.gerador)):
                        lista[i] = (lista[i] ^ self.gerador[i])
                else:
                    for i in range(len(self.gerador)):
                        lista[i] = (lista[i] ^ 0)
                
                lista.pop(0)
                lista.append(self.dados[cont])
                cont +=1
                
                
                #print("the cont2",cont)
                #print("A lista fffff",lista)
               
        lista.pop(0)
        self.crc = lista
        
    @property
    def enviar(self):
        for x in range(len(self.index)):
            self.dados[self.index[x]]+= self.crc[x]
        #print("Dados no final",self.dados)
        self.calcula_crc
        if(1 in self.crc):
            print("Houve ERRO na transmissão")
            
        else:
            print("Não houve erro na transmissão")
            
    @property
    def enviar_com_erro(self):
        for x in range(len(self.index)):
            self.dados[self.index[x]]+= self.crc[x]
        #print("Dados no final",self.dados)
        self.dados.append(self.dados[0])
        self.calcula_crc
        if(1 in self.crc):
            print("Houve ERRO na transmissão")
            
        else:
            print("Não houve erro na transmissão")
            
roda = True
while(roda!=False):
    print("Digite 1 para colocar o dado de envio")
    print("Digite 2 para digitar o polinomio")
    print("Digite 3 para gerar o CRC")
    print("Digite 4 para utilizar o Enviar")
    print("Digite 5 para simular um erro")
    print("Digite 6 para sair do programa")
    
    op = int(input("Escolha uma opção\n"))
    if(op==1):
        dado = str(input("Digite o dado para a transmissão\n"))
    if(op==2):
        poli = str(input("Digite o polinomio para a transmissão\n"))
    if(op==3):
        CRC = crc(dado,poli)
        CRC.calcula_polinomio
        CRC.calcula_crc
        print("CRC: ",CRC.crc)
        print("CRC gerado com sucesso")
    if(op==4):
        CRC.enviar
        print("CRC no enviar: ",CRC.crc)
    if(op==5):
        CRC.enviar_com_erro
        print("CRC no enviar: ",CRC.crc)
        print("Houve erro na transmissão pois o dado foi duplicado")
    if(op==6):
        print("PROGRAMA ENCERRADO!")
        roda = False
    
        
                  
        
