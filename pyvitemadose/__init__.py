"""
pyvitemadose init
"""

from os import sys
from pyvitemadose.args import compute_args, is_pyinstaller
from pyvitemadose.pyvitemadose import find
from pyvitemadose.update import update

def pyvitemadose():
    """
    pyvitemadose entry point
    """
    args = compute_args()

    if args.update:
        if not is_pyinstaller():
            update()
        else:
            print("update is disabled. Do you use a bundle?")
    if args.departement:
        find(args.departement)
    sys.exit(0)

pyvitemadose()