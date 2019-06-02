# -*- coding: utf-8 -*-
from GUI.gui_game import main as gui_main
from CLI.cli_game import main as cli_main


def launcher(appli = True):

    if appli == True:
        launchpad = gui_main
    else :
        launchpad = cli_main
    return launchpad()


def main():
    launcher(True)


if __name__ == "__main__":
    main()

 