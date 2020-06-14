import pygame
import sys
import numpy

ROW_COUNT = 7
COLUMN_COUNT = 7
MAX_RIGHT: int = 535
MAX_LEFT: int = 85
SCREEN_SIZE = 620
BOARD_SIZE = 520
MOVEMENT_DISTANCE = 75
CHIP_DIAMETER = 35


class Colors:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BACKGROUND = (0, 0, 123)
    CHOICE_BACKGROUND = (0, 150, 255)


def draw(rysx, rysy, screen, Board, ChoiceBackground, Array):
    pygame.draw.rect(screen, Colors.BLUE, Board)
    pygame.draw.rect(screen, Colors.CHOICE_BACKGROUND, ChoiceBackground)
    for x in range(0, COLUMN_COUNT):
        rysx += MOVEMENT_DISTANCE
        rysy = 10
        for y in range(0, ROW_COUNT):
            rysy += MOVEMENT_DISTANCE
            if Array[x][y] == 0:
                pygame.draw.circle(screen, Colors.BLACK, (rysx, rysy), CHIP_DIAMETER)
            else:
                chip(rysx, rysy, Array[x][y], screen)


def chip(Ccenterx, Ccentery, turn, screen):
    if turn == -1:
        pygame.draw.circle(screen, Colors.RED, (Ccenterx, Ccentery), CHIP_DIAMETER)
    elif turn == 1:
        pygame.draw.circle(screen, Colors.YELLOW, (Ccenterx, Ccentery), CHIP_DIAMETER)


def make_a_move(Array, turn, xpos):
    flag = True
    for y in range(COLUMN_COUNT - 1, 0, -1):
        if not flag:
            break
        ypos = y
        if Array[xpos][ypos] == 0:
            Array[xpos][ypos] = turn
            flag = False
    next_turn(turn)


def next_turn(turn):
    if turn == -1:
        turn += 2
    else:
        turn -= 2
    return turn


def check(Array, xpos, turn, myfont, screen):
    if Array[xpos][1] == 0:
        return True
    if Array[xpos][1] != 0:
        label = myfont.render("Forbidden Move", 1, Colors.YELLOW)
        screen.blit(label, (SCREEN_SIZE // 2 - label.get_width() // 2, SCREEN_SIZE // 2 - label.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)
        return False


def winning_move(Array, turn):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if Array[r][c] == turn and Array[r][c + 1] == turn and Array[r][c + 2] == turn and Array[r][c + 3] == turn:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if Array[r][c] == turn and Array[r + 1][c] == turn and Array[r + 2][c] == turn and Array[r + 3][c] == turn:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        if c + 3 != 0:
            for r in range(ROW_COUNT - 3):
                if Array[r][c] == turn and Array[r + 1][c + 1] == turn and Array[r + 2][c + 2] == turn and \
                        Array[r + 3][c + 3] == turn:
                    return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        if c + 3 != 0:
            for r in range(3, ROW_COUNT):
                if Array[r][c] == turn and Array[r - 1][c + 1] == turn and Array[r - 2][c + 2] == turn and \
                        Array[r - 3][c + 3] == turn:
                    return True

def checkdraw(tablica):
    flag = 0
    for x in range(0, COLUMN_COUNT):
        for y in range(1, ROW_COUNT):
            if tablica[x][y] == 0:
                flag = 1
    if flag == 0:
        return False
    else:
        return True




def main():
    pygame.init()
    centerx = 85
    centery = 85
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    board = pygame.Rect(50, 50, BOARD_SIZE, BOARD_SIZE)
    choicebackground = pygame.Rect(50, 50, BOARD_SIZE, 70)
    rysx = 10
    rysy = 10
    turn = -1
    game_over = False
    xpos = 0
    myfont = pygame.font.SysFont("monospace", 50)
    array = numpy.zeros([ROW_COUNT, COLUMN_COUNT])
    print(array)
    while not game_over:
        screen.fill(Colors.BACKGROUND)
        """Handle Events"""

        for event in pygame.event.get():
            # Closing game
            if event.type == pygame.QUIT:
                sys.exit(0)
            # Right movement
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if centerx == MAX_RIGHT:
                    centerx = MAX_LEFT
                    xpos = 0
                else:
                    centerx += MOVEMENT_DISTANCE
                    xpos += 1
            # Left movement
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if centerx == MAX_LEFT:
                    centerx = MAX_RIGHT
                    xpos = 6
                else:
                    centerx -= MOVEMENT_DISTANCE
                    xpos -= 1
            # Making a move
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if check(array, xpos, turn, myfont, screen):
                    make_a_move(array, turn, xpos)
                else:
                    turn = turn * (-1)
                if not winning_move(array, turn) and checkdraw(array):
                    turn = next_turn(turn)
                else:
                    if not checkdraw(array):
                        label = myfont.render("DRAW", 1, Colors.YELLOW)
                    elif turn == -1:
                        label = myfont.render("Player Red wins!!", 1, Colors.RED)
                    else:
                        label = myfont.render("Player Yellow wins!!", 1, Colors.YELLOW)
                    screen.blit(label, (SCREEN_SIZE // 2 - label.get_width() // 2, SCREEN_SIZE // 2 - label.get_height() // 2))
                    game_over = True
                    pygame.display.flip()
                    pygame.time.wait(3000)




            # drawing
            draw(rysx, rysy, screen, board, choicebackground, array)
            chip(centerx, centery, turn, screen)
            pygame.display.flip()
            if game_over:
                pygame.time.wait(2000)


if __name__ == '__main__':
    main()
