import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_maxpahse(chembl_id):
    try:
        chem_api = f'https://www.ebi.ac.uk/chembl/api/data/drug/{chembl_id}?format=json'
        res = requests.get(chem_api)
        res = res.json()
        return res.get('development_phase')
    except:
        return None

drugs = pd.read_csv('./drug_targets_dir_maxphase.csv')
drugs['Clinical_phase'] = 0
for i in drugs.index:
    drugs.at[i,'Clinical_phase'] = get_maxpahse(drugs.loc[i,'ChEMBL'])
    drugs.to_csv('./drug_targets_dir_maxphase.csv',index=False)
