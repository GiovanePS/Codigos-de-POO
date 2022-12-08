def print_board(board):
    for linha in board:
        for celula in linha:
            print(celula, end=" ")
        print()

def main():
    tamanho = 3
    board = [["." for _ in range(tamanho)] for _ in range(tamanho)]
    i = 0
    while i < 9:
        print_board(board)
        
        # Change turns
        if i % 2:
            symbol = "X"
        else:
            symbol = "O"
        
        # Move
        print(f"Player {i%2+1}")
        x, y = [ int(i) for i in input("x, y: ").split()]
        if x < 3 and y < 3:
            board[x][y] = symbol
        
        i += 1

if __name__ == "__main__":
    main()