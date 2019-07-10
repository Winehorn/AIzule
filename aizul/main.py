from aizul.GameController import GameController

def main(num_players=4):
    gc = GameController(num_players)
    gc.print_table()

if __name__ == "__main__":
    main()