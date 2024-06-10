"""
Copyright (C) 2012-2019 Craig Thomas
This project uses an MIT style license - see LICENSE for details.

A simple Chip 8 emulator - see the README file for more information.
"""
# I M P O R T S ###############################################################

import argparse
import os,sys
from tkinter import filedialog
from tkinter import Tk
# G L O B A L S ###############################################################

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# F U N C T I O N S  ##########################################################
def obtener_rom():
    root= Tk()
    root.geometry('0x0')
    root.iconify()
    #root.overrideredirect(True)
    file_path = filedialog.askopenfilename()
    root.destroy()
    if not file_path:
        sys.exit(0)
    return file_path

def parse_arguments():
    """
    Parses the command-line arguments passed to the emulator.

    :return: the parsed command-line arguments
    """
    parser = argparse.ArgumentParser(
        description="Starts a simple Chip 8 "
        "emulator. See README.md for more information, and LICENSE for "
        "terms of use.")
    parser.add_argument(
        "rom", help="the ROM file to load on startup", default=obtener_rom(), nargs="?")
    parser.add_argument(
        "--scale", help="the scale factor to apply to the display "
        "(default is 10)", type=int, default=10, dest="scale")
    parser.add_argument(
        "--delay", help="sets the CPU operation to take at least "
        "the specified number of milliseconds to execute (default is 1)",
        type=int, default=1, dest="op_delay")
    parser.add_argument("--notModern", help="use modern CHIP-i instructions", nargs="?", default=True, const=False, dest="modern")
    return parser.parse_args()


# M A I N #####################################################################

if __name__ == "__main__":
    from chip8.emulator import main_loop
    main_loop(parse_arguments())

# E N D   O F   F I L E #######################################################
