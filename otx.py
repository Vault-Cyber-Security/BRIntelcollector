#!/usr/bin/python3 

import requests
import json
from dotenv import load_dotenv
from dotenv import dotenv_values
from OTXv2 import OTXv2 
from OTXv2 import OTXv2, IndicatorTypes
import pandas 

load_dotenv()
#otx = OTXv2(str(dotenv_values('OTX_API_KEY')))
otx = OTXv2("1d676bb0a0c8f2e7be40b7636a86b5c9f977b668a787b8656662d2dd5eb37767")

#CONSULTAS PARA PULSES RELACIONADOS AO BRASIL
pulses=otx.search_pulses("Brazil")
p2=otx.search_pulses("BR")
p3=otx.search_pulses("Brasil")
#criação de dataframes
pdtable=pandas.DataFrame()
pd2 = pd.DataFrame()
pd3 = pd.DataFrame()
#criação de vetores temporários que auxiliam no manuseio dos dados
dta=[]
dta2=[]
dta3=[]
#ler resultados das querys e puchar os detalhes para obter mais dados das ocorrencias
for i in range(len(pulses["results"])):
        pulse_id=pulses["results"][i]["id"]
        pulse_details = otx.get_pulse_details(pulse_id) 
        dta.append(pulse_details)

for i in range(len(dta)): #montagem dataframe pdtable
        pdtable = pdtable.append(dta[i] , ignore_index=True)
for i in range(len(p2['results'])):
        p2_id=p2["results"][i]["id"]
        p2_details = otx.get_pulse_details(p2_id)
        dta2.append(p2_details)

for i in range(len(p3['results'])):
        p3_id=p3["results"][i]["id"]
        p3_details = otx.get_pulse_details(p3_id)
        dta3.append(p3_details)

#manuseio de resultados para montagem de dataframes pd2 e pd3
for i in range(len(dta2)):
  pd2 = pd2.append(dta2[i] , ignore_index=True)

for i in range(len(dta3)):
  pd3 = pd3.append(dta3[i] , ignore_index=True)

#montagem de dataframe final com os três dataframes concatenados
f=[pdtable,pd2,pd3] #variavel que armazena o conteúdo dos três dataframes
finalbr=pd.concat(f,ignore_index=True) #concatenação dos três dataframes

finalbr.to_csv('./otbrfinal.csv', index=False) #exportando o dataframe em um arquivo csv

#consulta personalizada por dominio
def consulta_dominio(otx):
    data=[]
    dominio=str(input('digite o dominio que deseja buscar'))
    dc=otx.search_pulses(dominio)
    domain_table=pd.DataFrame()
    for i in range(len(dc["results"])):
        pulse_id=dc["results"][i]["id"]
        pulse_details = otx.get_pulse_details(pulse_id)
        data.append(pulse_details)
    for i in range(len(data)):
        domain_table = domain_table.append(data[i] , ignore_index=True)
    domaintable.to_csv('./otxconsultadominio.csv',index=False)
