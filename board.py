def generate_board():
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ranks = list(range(8, 0, -1))

    board = []
    for rank in ranks:
        row = []
        for i, file in enumerate(files):
            coordinate = f"{file}{rank}"
            is_light = (i + rank) % 2 == 0
            color = "light" if is_light else "dark"
            row.append({
                "coordinate": coordinate,
                "file": file,
                "rank": rank,
                "color": color
            })
        board.append(row)
    return board


if __name__ == '__main__':
    board = generate_board()
    for row in board:
        print("  ".join(square['coordinate'] for square in row))



            