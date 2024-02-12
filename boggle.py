import random


def generate_boggle_board_string():
    """
    Return a new boggle-board-state string
    """

    dice = [
        "AEANEG",
        "AHSPCO",
        "ASPFFK",
        "OBJOAB",
        "IOTMUC",
        "RYVDEL",
        "LREIXD",
        "EIUNES",
        "WNGEEH",
        "LNHNRZ",
        "TSTIYD",
        "OWTOAT",
        "ERTTYL",
        "TOESSI",
        "TERWHV",
        "NUIHMQ",
    ]
    # Each dice goes into a random position
    random.shuffle(dice)

    # Iterate through each die and choose a random face to show.
    output = ""
    for die in dice:
        random_char = random.choice(die)
        output += random_char
    return output


# def board_to_string():

# def string_to_board():
#     row = []
#     board = []
#     return result


def display_board(board_string, x_space=1, y_space=1):
    """
    Prints a boggle board state string as a board.
    """
    # Split board_string into four substrings
    subs = [board_string[i : i + 4] for i in range(0, len(board_string), 4)]
    # Add spaces between characters
    rows = [" ".join(sub[i] + " " * x_space for i in range(len(sub))) for sub in subs]
    # Join the spaced substrings with newline characters and additional lines between rows
    board = ("\n" * y_space).join(rows)
    print(f"\n{board}")


def main():

    board = generate_boggle_board_string()
    display_board(board, 1, 2)


if __name__ == "__main__":
    main()
