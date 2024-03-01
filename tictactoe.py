import random

def print_board(board):
    # Виводить поточний стан дошки.
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Перевіряє, чи є переможець.
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def get_free_cells(board):
    # Повертає список вільних клітинок.
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def player_move(board):
    # Записує хід гравця.
    free_cells = get_free_cells(board)
    while True:
        try:
            row, col = map(int, input("Введіть рядок та стовпець (через пробіл): ").split())
            if (row - 1, col - 1) in free_cells:
                board[row - 1][col - 1] = "X"
                break
            else:
                print("Ця клітинка вже зайнята або не існує. Спробуйте ще раз.")
        except ValueError:
            print("Введені некоректні дані. Спробуйте ще раз.")

def computer_move(board):
    # Записує хід комп'ютера.
    free_cells = get_free_cells(board)
    row, col = random.choice(free_cells)
    board[row][col] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Початковий стан дошки:")
    print_board(board)
    while True:
        player_move(board)
        print("Ваш хід:")
        print_board(board)
        if check_winner(board, "X"):
            print("Ви виграли!")
            break
        if not get_free_cells(board):
            print("Нічия!")
            break
        computer_move(board)
        print("Хід комп'ютера:")
        print_board(board)
        if check_winner(board, "O"):
            print("Комп'ютер переміг!")
            break
        if not get_free_cells(board):
            print("Нічия!")
            break

if __name__ == "__main__":
    main()
