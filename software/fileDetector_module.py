#Funções do file detector module

import pandas as pd
csv = input("Nome do arquivo csv\n") #guarda o nome do arquivo .csv
log = pd.read_csv(csv) #lê o .csv

def tipo_csv_lc(log):
    #Retorna o tipo de log baseado no número de linhas/colunas
 
    linhas_colunas = list(log.shape) #lista com o número de linhas e colunas do .csv
    linhas_colunas[0] += 1 #por algum motivo conta uma coluna, então adiciono uma coluna à conta
  
    if(linhas_colunas[0] == 4):
        return "2D"
    elif(linhas_colunas[0] == 5):
        return "vss"
    elif(linhas_colunas[0] == 6):
        return "ssl"


def tipo_csv_termo(log):
    #retona o tipo de log baseado em termos conhecidos 
    termo_alvo = list(log)[0]
    if(termo_alvo == "termo_2d"):
        return "2D"
    elif(termo_alvo == "termo_vss"):
        return "vss"
    elif(termo_alvo == "termo_ssl"):
        return "ssl"
