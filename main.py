import sys
import random  
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
            parts = command.split() 
            
            if "startpos" in parts:
                board.set_fen(chess.STARTING_FEN) 
            
            if "moves" in parts:
                moves_index = parts.index("moves") + 1
                for move_uci in parts[moves_index:]:
                    board.push_uci(move_uci)

        elif command.startswith("go"):
            legal_moves = list(board.legal_moves)

            #zatím náhodný tah později tah podle algoritmu
            #todo: pridat algoritmus 
            if legal_moves:
                best_move = random.choice(legal_moves)
                print(f"bestmove {best_move.uci()}")
                sys.stdout.flush()


        elif command == "quit":
            break

if __name__ == "__main__":
    main()
