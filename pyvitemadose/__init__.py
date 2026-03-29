"""
pyvitemadose init
"""

from os import sys
from pyvitemadose.args import compute_args, is_pyinstaller
from pyvitemadose.pyvitemadose import find

def pyvitemadose():
    """
    pyvitemadose entry point
    """
    args = compute_args()

    if args.departement:
        find(args.departement)
    sys.exit(0)

pyvitemadose()