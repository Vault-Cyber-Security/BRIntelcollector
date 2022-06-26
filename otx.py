#!/usr/bin/python3 

import requests
import json
import datetime
from dotenv import load_dotenv
from dotenv import dotenv_values
from OTXv2 import OTXv2 
from OTXv2 import OTXv2, IndicatorTypes
import pandas 

load_dotenv()
otx = OTXv2(dotenv_values('OTXKey'))
#otx = OTXv2("")


pulses=otx.search_pulses("Brazil")
print(pandas.json_normalize(pulses["results"]))
pdtable=pandas.DataFrame()
for i in range(len(pulses["results"])):
        pulse_id=pulses["results"][i]["id"]
        pulse_details = otx.get_pulse_details(pulse_id)
        #pdtable.append(otx.get_pulse_details(pulse_id))
        print(pandas.json_normalize(pulse_details))


