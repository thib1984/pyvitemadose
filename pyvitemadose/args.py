"""
pygitscrum argparse gestion
"""

import argparse
import sys


def compute_args():
    """
    check args and return them
    """
    my_parser = argparse.ArgumentParser(
        description="pyvitemadose affiche les chronodoses disponibles du departement en parametre",
        epilog="""
        Full documentation at: <https://github.com/thib1984/pyvitemadose>.
        Report bugs to <https://github.com/thib1984/pyvitemadose/issues>.
        MIT Licence.
        Copyright (c) 2021 thib1984.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        Written by thib1984.""",
    )
    my_parser.add_argument(
        "departement",
        metavar="departement",
        type=int,
        help="numero departement",
    )

    # if no parameter
    if len(sys.argv) == 1:
        my_parser.print_help()
        sys.exit(0)

    args = my_parser.parse_args()
    return args
