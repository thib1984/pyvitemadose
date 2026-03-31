"""
pygitscrum argparse gestion
"""

import argparse
import sys
import importlib.metadata

def get_env_report():
    lines = []

    lines.append("\nInstalled packages:")
    for dist in sorted(importlib.metadata.distributions(), key=lambda d: d.metadata["Name"].lower()):
        name = dist.metadata["Name"]
        version = dist.version
        lines.append(f"  - {name}=={version}")
    
    return "\n".join(lines)

def compute_args():
    """
    check args and return them
    """
    my_parser = argparse.ArgumentParser(
        description="pyvitemadose displays available schedules of covid vaccine for your departement in France given in parameter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
To upgrade, run:
    pipx upgrade pyvitemadose
    pipx reinstall pyvitemadose #to force update dependencies
To install, run:
    pipx install pyvitemadose
To force reinstall, run:
    pipx install pyvitemadose --force
To uninstall, run:
    pipx uninstall pyvitemadose
To force uninstall (if needed), run:
    pipx uninstall pyvitemadose --force

{get_env_report()}

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
        type=str,
        nargs="?",
        help="numero departement",
    )
    my_parser.add_argument(
        "-b",
        "--before",
        metavar="before",
        type=str,
        nargs="?",
        help="before date yyyy-mm-dd",
    )    
    my_parser.add_argument(
        "-n",
        "--nocolor",
        action="store_true",
        help="disable colors and emojis in sysout",
    )

    # if no parameter
    if len(sys.argv) == 1:
        my_parser.print_help()
        sys.exit(0)

    args = my_parser.parse_args()
    return args


def is_pyinstaller():
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')