"""
pyvitemadose init
"""

from os import sys
from pyvitemadose.args import compute_args
from pyvitemadose.pyvitemadose import find

def pyvitemadose():
    """
    pyvitemadose entry point
    """
    args = compute_args()

    if args.update:
        try:
            from pyvitemadose.update import update
            update()
        except ImportError:
            print("update is disabled. You seem to use autoexec version")    
    if args.departement:
        find(args.departement)
    sys.exit(0)

pyvitemadose()