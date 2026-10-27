import sys
import chess

def main():

    board = chess.Board()

    while True:
        command = sys.stdin.readline().strip()

        if not command:
            continue

        if command == "uci":
            print("id name ChessBot")
            print("id author JanKoverdynsky")
            print("uciok")
            sys.stdout.flush()  

        elif command == "isready":
            print("readyok") 
            sys.stdout.flush()

        elif command.startswith("position"):
            if "startpos" in command:
                board.set_fen(chess.STARTING_FEN) #notace nastavit board na startovní pozici


        elif command == "quit":
            break

if __name__ == "__main__":
    main()
