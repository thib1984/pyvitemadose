"""
pyvitemadose use case
"""

import argparse
import sys
import requests

def find(dept):
    trouve = False
    r = requests.get("https://vitemadose.gitlab.io/vitemadose/"+dept.zfill(2)+".json")
    if str(r) != "<Response [200]>":
        print(str(r) + " : no data found, verify the departement")
        sys.exit(1)
    for centre in r.json().get("centres_disponibles",[]):
        if centre.get("appointment_count","") != 0:
            trouve = True
            print("url      : " + centre.get("url"))
            print("adresse  : " + centre.get("metadata").get("address"))
            print("type     : " + str(centre.get("vaccine_type")))
            print("doses    : " + str(centre.get("appointment_count")))    
            print("")                          
    if not trouve:
        print("pas de creneaux trouves...")
        sys.exit(2)
