import pygame, sys, numpy

ROW_COUNT = 7
COLUMN_COUNT = 7
MAX_RIGHT: int = 535
MAX_LEFT: int = 85

pygame.init()

class Colors:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
def Draw(rysx, rysy,screen,Board,ChoiceBackground,Array):
    pygame.draw.rect(screen, Colors.BLUE, Board)
    pygame.draw.rect(screen, (0, 150, 255), ChoiceBackground)
    for x in range(0, COLUMN_COUNT):
        rysx += 75
        rysy = 10
        for y in range(0, ROW_COUNT):
            rysy += 75
            if Array[x][y] == 0:
                pygame.draw.circle(screen, Colors.BLACK, (rysx, rysy), 35)
            else:
                Chip(rysx, rysy, Array[x][y],screen)
            # pygame.draw.circle(screen, BLACK, (rysx, rysy), 35)


def Chip(Ccenterx, Ccentery, turn, screen):
    if turn == -1:
        pygame.draw.circle(screen, Colors.RED, (Ccenterx, Ccentery), 35)
    elif turn == 1:
        pygame.draw.circle(screen, Colors.YELLOW, (Ccenterx, Ccentery), 35)


def Make_A_Move(Array, turn, xpos):
    flag = True
    for y in range(6, 0, -1):
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
        screen.blit(label, (310 - label.get_width() // 2, 310 - label.get_height() // 2))
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

def main():
    Ccenterx = 85
    Ccentery = 85
    screen = pygame.display.set_mode((620, 620))
    Board = pygame.Rect(50, 50, 520, 520)
    ChoiceBackground = pygame.Rect(50, 50, 520, 70)
    rysx = 10
    rysy = 10
    turn = -1
    game_over = False
    xpos = 0
    myfont = pygame.font.SysFont("monospace", 50)
    Array = numpy.zeros([ROW_COUNT, COLUMN_COUNT])
    print(Array)
    while not game_over:
        screen.fill((0, 0, 123))
        # Handle Events

        for event in pygame.event.get():
            # Closing game
            if event.type == pygame.QUIT:
                sys.exit(0)
            # Right movement
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if Ccenterx == MAX_RIGHT:
                    Ccenterx = MAX_LEFT
                    xpos = 0
                else:
                    Ccenterx += 75
                    xpos += 1
            # Left movement
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if Ccenterx == MAX_LEFT:
                    Ccenterx = MAX_RIGHT
                    xpos = 6
                else:
                    Ccenterx -= 75
                    xpos -= 1
            # Making a move
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if check(Array, xpos, turn,myfont,screen):
                    Make_A_Move(Array, turn, xpos)
                else:
                    turn = turn * (-1)
                if not winning_move(Array, turn):
                    turn = next_turn(turn)
                else:
                    if turn == -1:
                        label = myfont.render("Player Red wins!!", 1, Colors.RED)
                    else:
                        label = myfont.render("Player Yellow wins!!", 1, Colors.YELLOW)
                    screen.blit(label, (310 - label.get_width() // 2, 310 - label.get_height() // 2))
                    game_over = True
                    pygame.display.flip()
                    pygame.time.wait(3000)

            # drawing
            Draw(rysx, rysy, screen, Board, ChoiceBackground, Array)
            Chip(Ccenterx, Ccentery, turn,screen)
            pygame.display.flip()
            if game_over:
                pygame.time.wait(2000)
main()
