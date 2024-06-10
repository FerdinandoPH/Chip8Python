"""
Copyright (C) 2012-2019 Craig Thomas
This project uses an MIT style license - see LICENSE for details.

A simple Chip 8 emulator - see the README file for more information.
"""
# I M P O R T S ###############################################################

import pygame
TIMER = pygame.USEREVENT + 1
from chip8.config import FONT_FILE, DELAY_INTERVAL
from chip8.cpu import Chip8CPU
from chip8.screen import Chip8Screen
from chip8.state import State
import pickle
from copy import deepcopy
# C O N S T A N T S ###########################################################

# A simple timer event used for the delay and sound timers


# F U N C T I O N S  ##########################################################


def main_loop(args):
    """
    Runs the main emulator loop with the specified arguments.

    :param args: the parsed command-line arguments
    """
    screen = Chip8Screen(scale_factor=args.scale)
    screen.init_display()
    cpu = Chip8CPU(screen,args.modern, args.op_delay)
    cpu.load_rom(FONT_FILE, 0)
    cpu.load_rom(args.rom)
    #cpu.debug=True
    pygame.init()
    pygame.time.set_timer(TIMER, DELAY_INTERVAL)

    while cpu.running:
        pygame.time.wait(args.op_delay)
        cpu.execute_instruction()
        if cpu.op_delay!=args.op_delay:
            args.op_delay=cpu.op_delay
        # Check for events
        #print(pygame.event.get())
        for event in pygame.event.get():
            if event.type == TIMER:
                cpu.decrement_timers()
            elif event.type == pygame.QUIT:
                cpu.running = False
            elif event.type == pygame.KEYDOWN:
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_ESCAPE]:
                    print("Initiating debug mode")
                    cpu.debug = True
                elif keys_pressed[pygame.K_F5]:
                    print("Saving state...")
                    cpu.screen=None
                    state=State(deepcopy(cpu),screen.save_state()[0],screen.save_state()[1],screen.save_state()[2],screen.save_state()[3])
                    cpu.screen=screen
                    print(args.rom)
                    print(args.rom.split("/")[-1]+"_state.dat")
                    with open(args.rom.split("/")[-1]+"_state.dat","wb") as f:
                        pickle.dump(state,f)
                elif keys_pressed[pygame.K_F7]:
                    print("Loading state...")
                    try:
                        with open(args.rom.split("/")[-1]+"_state.dat","rb") as f:
                            state=pickle.load(f)
                    except OSError:
                        print("No state file found")
                    else:
                        cpu=state.cpu
                        cpu.screen=screen
                        screen.load_state(state.scale_factor,state.width,state.height,state.screen_array)
                    

# E N D   O F   F I L E #######################################################
