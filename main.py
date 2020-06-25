"""Connect 4"""
import math
import numpy
import pygame
import random
import sys




ROW_COUNT = 7
COLUMN_COUNT = 7
MAX_RIGHT: int = 535
MAX_LEFT: int = 85
SCREEN_SIZE = 620
BOARD_SIZE = 520
MOVEMENT_DISTANCE = 75
CHIP_DIAMETER = 35
BOARD_POS = 50
CHOICE_BACKGROUND_WIDTH = 70
PLAYER = -1
AI = 1
EMPTY = 0
WINDOW_LENGTH = 4


class Colors:
    PLAYBOARD = (38, 139, 210)
    EMPTY_SPACE = (0, 0, 0)
    RED_CHIP = (220, 50, 47)
    YELLOW_CHIP = (181, 137, 0)
    BACKGROUND = (0, 43, 54)
    CHOICE_BACKGROUND = (101, 123, 131)


def draw(position_x_draw, position_y_draw, screen, board, choice_background, array):
    """It draws board and chips"""
    pygame.draw.rect(screen, Colors.PLAYBOARD, board)
    pygame.draw.rect(screen, Colors.CHOICE_BACKGROUND, choice_background)
    for x_position in range(0, COLUMN_COUNT):
        position_x_draw += MOVEMENT_DISTANCE
        position_y_draw = 10
        for y_position in range(0, ROW_COUNT):
            position_y_draw += MOVEMENT_DISTANCE
            if array[y_position][x_position] == 0:
                pygame.draw.circle(screen, Colors.EMPTY_SPACE,
                                   (position_x_draw, position_y_draw), CHIP_DIAMETER)
            else:
                chip(position_x_draw, position_y_draw, array[y_position][x_position], screen)


def chip(centerx, centery, turn, screen):
    """It decides which chip should be drawn and also it draws  it on given position"""
    if turn == -1:
        pygame.draw.circle(screen, Colors.RED_CHIP, (centerx, centery), CHIP_DIAMETER)
    elif turn == 1:
        pygame.draw.circle(screen, Colors.YELLOW_CHIP, (centerx, centery), CHIP_DIAMETER)


def make_a_move(array, turn, x_array_position):
    """Checks if a position is taken and if so it gives your chip one above if possible"""
    flag = True
    for i in range(COLUMN_COUNT - 1, 0, -1):
        if not flag:
            break
        y_array_position = i
        if array[y_array_position][x_array_position] == 0:
            array[y_array_position][x_array_position] = turn
            flag = False
    next_turn(turn)


def next_turn(turn):
    """It switches turns"""
    if turn == PLAYER:
        return AI
    else:
        return PLAYER


def check(array, x_array_position, my_font, screen):
    """Checks if move is forbidden"""
    if array[1][x_array_position] == 0:
        return True
    else:
        label = my_font.render("Forbidden Move", 1, Colors.YELLOW_CHIP)
        screen.blit(label, (SCREEN_SIZE // 2 - label.get_width() // 2,
                            SCREEN_SIZE // 2 - label.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)
        return False


def winning_move(array, turn):
    """Checks if someone already won"""
    # Check horizontal locations for win
    for i in range(COLUMN_COUNT - 3):
        for j in range(ROW_COUNT):
            if array[j][i] == array[j][i + 1] == array[j][i + 2] == array[j][i + 3] == turn:
                return True

    # Check vertical locations for win
    for i in range(COLUMN_COUNT):
        for j in range(ROW_COUNT - 3):
            if array[j][i] == array[j + 1][i] == array[j + 2][i] == array[j + 3][i] == turn:
                return True

    # Check positively sloped diagonal
    for i in range(COLUMN_COUNT - 3):
        if i + 3 != 0:
            for j in range(ROW_COUNT - 3):
                if array[j][i] == array[j + 1][i + 1] == array[j + 2][i + 2] == array[j + 3][i + 3] == turn:
                    return True

    # Check negatively sloped diagonal
    for i in range(COLUMN_COUNT - 3):
        if i + 3 != 0:
            for j in range(3, ROW_COUNT):
                if array[j][i] == array[j - 1][i + 1] == array[j - 2][i + 2] == array[j - 3][i + 3] == turn:
                    return True


def check_draw(array):
    """Checks if there is draw on a board and there are no free moves left"""
    flag = False
    for x_position in range(0, COLUMN_COUNT):
        for y_position in range(1, ROW_COUNT):
            if array[y_position][x_position] == 0:
                flag = True
    return flag


def make_a_move_ai(array, row, col, turn):
    """AI makes a move"""
    array[row][col] = turn


def check_valid_location(array, col):
    """Checks if location is  used"""
    return array[ROW_COUNT - 2][col] == 0


def check_open_row(array, col):
    """Gives next open row"""
    for r in range(ROW_COUNT):
        if array[r][col] == 0:
            return r


def evaluate_window(window, turn):
    """evaluates window"""
    score = 0
    opp_piece = PLAYER
    if turn == PLAYER:
        opp_piece = AI

    if window.count(turn) == 4:
        score += 100
    elif window.count(turn) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(turn) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def check_score(array, turn):
    """Gives scores for move"""
    score = 0

    ## Score center column
    center_array = [int(i) for i in list(array[:, COLUMN_COUNT // 2])]
    center_count = center_array.count(turn)
    score += center_count * 3

    ## Score Horizontal
    for r in range(ROW_COUNT - 1):
        row_array = [int(i) for i in list(array[r, :])]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c + WINDOW_LENGTH]
            score += evaluate_window(window, turn)

    ## Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(array[:, c])]
        for r in range(ROW_COUNT - 4):
            window = col_array[r:r + WINDOW_LENGTH]
            score += evaluate_window(window, turn)

    ## Score posiive sloped diagonal
    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT - 3):
            window = [array[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, turn)

    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT - 3):
            window = [array[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, turn)

    return score


def is_terminal_node(array):
    """checks if someone won or there is no more moves"""
    return winning_move(array, PLAYER) or winning_move(array, AI) or len(list_valid_locations(array)) == 0


def mini_max(array, depth, alpha, beta, maximizing_player):
    valid_locations = list_valid_locations(array)
    is_terminal = is_terminal_node(array)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(array, AI):
                return None, 100000000000000
            elif winning_move(array, PLAYER):
                return None, -10000000000000
            else:
                return None, 0
        else:
            return None, check_score(array, AI)
    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:

            row = check_open_row(array, col)
            b_copy = array.copy()

            make_a_move_ai(b_copy, row, col, AI)

            new_score = mini_max(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = check_open_row(array, col)
            b_copy = array.copy()
            make_a_move_ai(b_copy, row, col, PLAYER)
            new_score = mini_max(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def list_valid_locations(array):
    """Returns list of valid locations"""
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if check_valid_location(array, col):
            valid_locations.append(col)
    return valid_locations


def pick_best_move(array, turn):
    """AI picks the best move"""
    valid_locations = list_valid_locations(array)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = check_open_row(array, col)
        temp_board = array.copy()
        make_a_move_ai(temp_board, row, col, turn)
        score = check_score(temp_board, turn)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col


def main():
    """Main function"""
    pygame.init()
    centerx = 85
    centery = 85
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    board = pygame.Rect(BOARD_POS, BOARD_POS, BOARD_SIZE, BOARD_SIZE)
    choice_background = pygame.Rect(BOARD_POS, BOARD_POS, BOARD_SIZE, CHOICE_BACKGROUND_WIDTH)
    position_x_draw = 10
    position_y_draw = 10
    turn = -1
    game_over = False
    x_array_position = 0
    my_font = pygame.font.SysFont("monospace", 50)
    array = numpy.zeros([ROW_COUNT, COLUMN_COUNT])
    print(array)
    while not game_over:
        screen.fill(Colors.BACKGROUND)
        # Handle Events
        if turn == PLAYER:
            for event in pygame.event.get():
                # Closing game
                if event.type == pygame.QUIT:
                    sys.exit(0)
                # Right movement
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    if centerx == MAX_RIGHT:
                        centerx = MAX_LEFT
                        x_array_position = 0
                    else:
                        centerx += MOVEMENT_DISTANCE
                        x_array_position += 1
                # Left movement
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    if centerx == MAX_LEFT:
                        centerx = MAX_RIGHT
                        x_array_position = 6
                    else:
                        centerx -= MOVEMENT_DISTANCE
                        x_array_position -= 1
                # Making a move
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if check(array, x_array_position, my_font, screen):
                        make_a_move(array, turn, x_array_position)
                        print(array)
                    else:
                        turn = turn * (-1)
                    if not winning_move(array, turn) and check_draw(array):
                        turn = next_turn(turn)
                    else:
                        if not check_draw(array):
                            label = my_font.render("DRAW", 1, Colors.YELLOW_CHIP)
                        elif turn == -1:
                            label = my_font.render("Player Red wins!!", 1, Colors.RED_CHIP)
                        screen.blit(label, (
                            SCREEN_SIZE // 2 - label.get_width() // 2, SCREEN_SIZE // 2 - label.get_height() // 2))
                        game_over = True
                        pygame.display.flip()
                        pygame.time.wait(3000)
        else:
            array = numpy.flip(array)
            col, minimax_score = mini_max(array, 5, -math.inf, math.inf, True)
            if check_valid_location(array, col):
                row = check_open_row(array, col)
                make_a_move_ai(array, row, col, AI)
                turn = next_turn(turn)
                if winning_move(array, AI):
                    label = my_font.render("AI wins!!", 1, Colors.YELLOW_CHIP)
                    screen.blit(label, (
                        SCREEN_SIZE // 2 - label.get_width() // 2, SCREEN_SIZE // 2 - label.get_height() // 2))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    game_over = True
            array = numpy.flip(array)

        # drawing
        draw(position_x_draw, position_y_draw, screen, board, choice_background, array)
        chip(centerx, centery, turn, screen)
        pygame.display.flip()
        if game_over:
            pygame.time.wait(2000)


if __name__ == '__main__':
    main()
