import matplotlib.pyplot as plt
import life_game as lg


def main():
    rows = 40
    columns = 40
    iterations = 100
    sizeup = 10

    board = lg.init_board(rows, columns)
    paddedBoard = lg.pad_board(board)

    for it in range(iterations):
        nextBoard = lg.get_next_board(paddedBoard)
        paddedBoard = lg.pad_board(nextBoard)

        biggerBoard = nextBoard.repeat(sizeup, axis=0)
        biggerBoard = biggerBoard.repeat(sizeup, axis=1)

        # im = Image.fromarray(biggerBoard,'1')
        plt.imshow(biggerBoard,'gray')
        plt.savefig(str("results/test%d.png" % it), bbox_inches='tight')


main()
