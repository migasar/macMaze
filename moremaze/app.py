# -*- coding: utf-8 -*-
from GUI.gui_game import main as gui_main
from CLI.cli_game import main as cli_main


def launcher(appli):

    if appli == 'pygame':
        launchpad = gui_main
    elif appli == 'terminal':
        launchpad = cli_main
    return launchpad()


def main():
    # launcher(pygame)
    launcher('terminal')


if __name__ == "__main__":
    main()

 