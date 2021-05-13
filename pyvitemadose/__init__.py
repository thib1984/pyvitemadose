"""
pyvitemadose init
"""


from pyvitemadose.args import compute_args
from pyvitemadose.pyvitemadose import find
from pyvitemadose.update import update

def pyvitemadose():
    """
    pyvitemadose entry point
    """
    args = compute_args()


    if args.update:
        update()
    if args.departement:
        find(args.departement)
