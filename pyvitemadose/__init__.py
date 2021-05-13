"""
pyvitemadose init
"""


from pyvitemadose.args import compute_args
from pyvitemadose.pyvitemadose import find

def pyvitemadose():
    """
    pyvitemadose entry point
    """
    args = compute_args()

    if args.departement:
        find(args.departement)
