"""
pyvitemadose use case
"""

import sys
import requests
import re

from pyvitemadose.args import compute_args


def find(dept):

    if compute_args().before and not re.match(
        "[0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]",
        str(compute_args().before),
    ):
        print(
            str(compute_args().before)
            + " : no valid format date, use yyyy-mm-dd format please"
        )
        sys.exit(1)
    trouve = False
    r = requests.get(
        "https://vitemadose.gitlab.io/vitemadose/"
        + dept.zfill(2)
        + ".json"
    )
    if str(r) != "<Response [200]>":
        print(str(r) + " : no data found, verify the departement")
        sys.exit(1)
    for centre in r.json().get("centres_disponibles", []):
        if centre.get("appointment_count", "") != 0:
            if (
                not compute_args().before
                or str(centre.get("prochain_rdv")[0:10])
                <= compute_args().before
            ):
                trouve = True
                print(
                    "1er rdv disp. : "
                    + str(centre.get("prochain_rdv")[0:10])
                )
                print("url           : " + centre.get("url"))
                print(
                    "adresse       : "
                    + centre.get("metadata").get("address")
                )
                print(
                    "type          : "
                    + str(centre.get("vaccine_type"))
                )
                print(
                    "doses         : "
                    + str(centre.get("appointment_count"))
                )
                print("")
    if not trouve:
        print("pas de creneaux trouves...")
        sys.exit(2)
