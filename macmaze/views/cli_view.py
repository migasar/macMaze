"""
Manage the display of every elements of the game
"""

from config import constants


class CLIview:

    def __init__(self, board):
        self.board = board

    def display_board(self):
        """Display the board line by line in the terminal"""

        print("")
        display_grid = []

        for y, line in enumerate(self.board.grid):

            display_line = ""
            for block in self.board.grid[y]:
                if block.toping:
                    display_line += block.toping
                else:
                    display_line += block.visual
            display_grid.append(display_line)

        for line in display_grid:
            print(line)

    def display_title(self):
        """Display a title in the terminal to indicate the start of the game"""

        print("")
        print("\t**********************************************")
        print(
            "\t  " + constants.GAME_TITLE
            + " - " + constants.GAME_BID
            )
        print("\t**********************************************")

    ######
    # methods to display the end of the game
    def display_goodbye(self):
        """Display a text indicating the end of the game"""

        print("")
        print("\t**********************************************")
        print("\t Vous quittez le jeu.")
        print("")

    def display_victory(self):
        """Display a text indicating that you won the game"""

        print("")
        print("\t**********************************************")
        print("\t Bravo, vous avez trouvé le chemin du labyrinthe,")
        print("")

    def display_defeat(self):
        """Display a text indicating that you lost the game"""

        print("")
        print("\t**********************************************")
        print("\t Désolé, le gardien a vaincu MacGyver.")
        print("")

    ######
    # methods to display a problem with the action
    def display_failure_input(self):
        """Display a text indicating an error in a command"""

        print("")
        print("\t Désolé, votre commande n'est pas valide.")

    def display_no_motion(self):
        """Display a text indicating that a move is not playable"""

        print("")
        print("\t Mac Gyver ne peut pas aller par là.")

    ######
    # methods to display information to the player
    def display_explanation(self):
        """
        Display a text indicating the rules of the game
        and the commands available
        """

        print("")
        print("\t Dirigez MacGyver jusqu'à la sortie du labyrinthe")
        print("\t  - pour aller en haut, appuyez sur S")
        print("\t  - pour aller en bas, appuyez sur X")
        print("\t  - pour aller à gauche, appuyez sur W")
        print("\t  - pour aller à droite, appuyez sur C")
        print("\t  - pour quitter le jeu, appuyez sur Q")

    def display_invitation(self):
        """Method to get an order from the player"""

        print("")
        self.new_order = input("Qu'allez vous faire ?  ")
        return self.new_order
