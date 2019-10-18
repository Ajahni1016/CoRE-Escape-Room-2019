#This is our main - Nothing really needed to do here other than import controller and call the function that runs the game.
from src import Controller
def main():
    main_window = Controller.Controller()
    main_window.mainLoop()
main()
