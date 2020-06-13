import pygame, sys, numpy

ROW_COUNT = 7
COLUMN_COUNT = 7
MAX_RIGHT: int = 535
MAX_LEFT: int = 85
tablica = numpy.zeros([ROW_COUNT, COLUMN_COUNT])
print(tablica)
pygame.init()
Ccenterx = 85
Ccentery = 85
screen = pygame.display.set_mode((620, 620))
plansza = pygame.Rect(50, 50, 520, 520)
wybór = pygame.Rect(50, 50, 520, 70)
rysx = 10
rysy = 10
tura = -1
game_over = False
xpos = 0
myfont = pygame.font.SysFont("monospace", 50)
class Colors:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
def Rysuj(rysx, rysy):
    pygame.draw.rect(screen, Colors.BLUE, plansza)
    pygame.draw.rect(screen, (0, 150, 255), wybór)
    for x in range(0, COLUMN_COUNT):
        rysx += 75
        rysy = 10
        for y in range(0, ROW_COUNT):
            rysy += 75
            if tablica[x][y] == 0:
                pygame.draw.circle(screen, Colors.BLACK, (rysx, rysy), 35)
            else:
                Krazek(rysx, rysy, tablica[x][y])
            # pygame.draw.circle(screen, BLACK, (rysx, rysy), 35)


def Krazek(Ccenterx, Ccentery, tura):
    if tura == -1:
        pygame.draw.circle(screen, Colors.RED, (Ccenterx, Ccentery), 35)
    elif tura == 1:
        pygame.draw.circle(screen, Colors.YELLOW, (Ccenterx, Ccentery), 35)


def Ruch(tablica, tura, xpos):
    flag = True
    for y in range(6, 0, -1):
        if not flag:
            break
        ypos = y
        if tablica[xpos][ypos] == 0:
            tablica[xpos][ypos] = tura
            flag = False
    nextTurn(tura)


def nextTurn(tura):
    if tura == -1:
        tura += 2
    else:
        tura -= 2
    return tura
def check(tablica,xpos,tura):
    if tablica[xpos][1] == 0:
        return True
    if tablica[xpos][1] != 0:
        label = myfont.render("Forbidden Move", 1, Colors.YELLOW)
        screen.blit(label, (310 - label.get_width() // 2, 310 - label.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)
        return False

def winning_move(tablica, tura):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if tablica[r][c] == tura and tablica[r][c + 1] == tura and tablica[r][c + 2] == tura and tablica[r][c + 3] == tura:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 4):
            if tablica[r][c] == tura and tablica[r + 1][c] == tura and tablica[r + 2][c] == tura and tablica[r + 3][c] == tura:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 4):
        for r in range(ROW_COUNT - 4):
            if tablica[r][c] == tura and tablica[r + 1][c + 1] == tura and tablica[r + 2][c + 2] == tura and \
                    tablica[r + 3][c + 3] == tura:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 4):
        for r in range(4, ROW_COUNT):
            if tablica[r][c] == tura and tablica[r - 1][c + 1] == tura and tablica[r - 2][c + 2] == tura and \
                    tablica[r - 3][c + 3] == tura:
                return True


while not game_over:
    screen.fill((0, 0, 123))
    # Handle Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if Ccenterx == MAX_RIGHT:
                Ccenterx = MAX_LEFT
                xpos = 0
            else:
                Ccenterx += 75
                xpos += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if Ccenterx == MAX_LEFT:
                Ccenterx = MAX_RIGHT
                xpos = 6
            else:
                Ccenterx -= 75
                xpos -= 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if check(tablica,xpos,tura):
                Ruch(tablica, tura, xpos)
            else:
                tura = tura * (-1)
            if not winning_move(tablica, tura):
                tura = nextTurn(tura)
            else:
                if tura == -1:
                    label = myfont.render("Player Red wins!!", 1, Colors.RED)
                else:
                    label = myfont.render("Player Yellow wins!!", 1, Colors.YELLOW)
                screen.blit(label, (310 - label.get_width() // 2, 310 - label.get_height() // 2))
                game_over = True
                pygame.display.flip()
                pygame.time.wait(3000)

        # drawing
        Rysuj(rysx, rysy)
        Krazek(Ccenterx, Ccentery, tura)
        pygame.display.flip()

