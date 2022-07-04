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


pulses=otx.search_pulses("Brazil")
#print(pandas.json_normalize(pulses["results"]))
pdtable=pandas.DataFrame()
dta=[]
for i in range(len(pulses["results"])):
        pulse_id=pulses["results"][i]["id"]
        pulse_details = otx.get_pulse_details(pulse_id) 
        dta.append(pulse_details)

for i in range(len(dta)):
        pdtable = pdtable.append(dta[i] , ignore_index=True)

pdtable.to_csv('./otxbr.csv',index=False)      
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
