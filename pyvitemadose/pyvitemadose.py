"""
pyvitemadose argparse gestion
"""

import argparse
import sys
import requests

def find(dept):
    trouve = False
    r = requests.get("https://vitemadose.gitlab.io/vitemadose/"+str(dept)+".json")
    centres_disponibles = r.json().get("centres_disponibles",[])
    for centre in centres_disponibles:
        appointment_schedules =  centre.get("appointment_schedules",[])
        for schedule in appointment_schedules:
            if schedule.get("name","") == "chronodose" and schedule.get("total","") != 0:
                trouve = True
                print("url      : " + centre.get("url"))
                print("adresse  : " + centre.get("metadata").get("address"))
                print("type     : " + str(centre.get("vaccine_type")))
                print("doses    : " + str(schedule.get("total")))    
                print("")                           
    if not trouve:
        print("pas de creneaux trouves...")
        sys.exit(2)