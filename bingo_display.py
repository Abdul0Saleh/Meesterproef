import pygame
import threading

_state = {
    "running": False,
    "cards": [None, None],
    "marked": [set(), set()],
    "active_team": 0,
    "highlight_number": None,
}
_lock = threading.Lock()
_thread = None

BG          = (30,  30,  46)
CARD_BG     = (49,  50,  68)
CELL_NORMAL = (69,  71,  90)
CELL_MARKED = (166, 227, 161)
CELL_FLASH  = (249, 226, 175)
TEXT_LIGHT  = (205, 214, 244)
TEXT_DARK   = (30,  30,  46)
HEADER_T1   = (137, 180, 250)
HEADER_T2   = (243, 139, 168)
ACTIVE_GLOW = (166, 227, 161)
INACTIVE    = (88,  91, 112)

CELL_SIZE = 80
GAP       = 4
PADDING   = 20
COLS      = 4
ROWS      = 4
CARD_W    = COLS * CELL_SIZE + (COLS + 1) * GAP
CARD_H    = ROWS * CELL_SIZE + (ROWS + 1) * GAP
WIN_W     = PADDING * 3 + CARD_W * 2
WIN_H     = PADDING * 4 + 50 + CARD_H


def _cell_rect(card_x, card_y, col, row):
    x = card_x + GAP + col * (CELL_SIZE + GAP)
    y = card_y + GAP + row * (CELL_SIZE + GAP)
    return pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)


def _draw_card(surface, font_big, team_idx, card_x, card_y, active):
    with _lock:
        card    = _state["cards"][team_idx]
        marked  = set(_state["marked"][team_idx])
        highlight = _state["highlight_number"]

    if card is None:
        return

    color      = CARD_BG if active else (40, 40, 55)
    border_col = ACTIVE_GLOW if active else INACTIVE
    pygame.draw.rect(surface, color,      (card_x, card_y, CARD_W, CARD_H), border_radius=12)
    pygame.draw.rect(surface, border_col, (card_x, card_y, CARD_W, CARD_H), 3, border_radius=12)

    for row_i, row in enumerate(card):
        for col_i, num in enumerate(row):
            rect      = _cell_rect(card_x, card_y, col_i, row_i)
            is_marked = num in marked
            is_flash  = (highlight is not None and num == highlight)

            if is_flash:
                cell_color, text_color = CELL_FLASH,  TEXT_DARK
            elif is_marked:
                cell_color, text_color = CELL_MARKED, TEXT_DARK
            else:
                cell_color, text_color = CELL_NORMAL, TEXT_LIGHT

            pygame.draw.rect(surface, cell_color, rect, border_radius=8)
            txt = font_big.render(str(num), True, text_color)
            surface.blit(txt, txt.get_rect(center=rect.center))


def _pygame_loop(card1, card2):
    pygame.init()
    screen = pygame.display.set_mode((WIN_W, WIN_H))
    pygame.display.set_caption("Lingo Bingo — Bingo Cards")
    clock = pygame.time.Clock()

    font_title = pygame.font.SysFont("Arial", 26, bold=True)
    font_big   = pygame.font.SysFont("Arial", 28, bold=True)
    font_small = pygame.font.SysFont("Arial", 14)

    with _lock:
        _state["cards"][0] = card1
        _state["cards"][1] = card2
        _state["running"]  = True

    card1_x = PADDING
    card2_x = PADDING * 2 + CARD_W
    card_y  = PADDING * 2 + 50
    flash_timer = 0

    while True:
        with _lock:
            still_running = _state["running"]
        if not still_running:
            break

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with _lock:
                    _state["running"] = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for team_idx, cx in enumerate([card1_x, card2_x]):
                    with _lock:
                        card = _state["cards"][team_idx]
                    if card is None:
                        continue
                    for row_i, row in enumerate(card):
                        for col_i, num in enumerate(row):
                            if _cell_rect(cx, card_y, col_i, row_i).collidepoint(mx, my):
                                with _lock:
                                    if num in _state["marked"][team_idx]:
                                        _state["marked"][team_idx].discard(num)
                                    else:
                                        _state["marked"][team_idx].add(num)

        with _lock:
            hl = _state["highlight_number"]
        if hl is not None:
            flash_timer += 1
            if flash_timer > 60:
                with _lock:
                    _state["highlight_number"] = None
                flash_timer = 0
        else:
            flash_timer = 0

        screen.fill(BG)

        with _lock:
            active = _state["active_team"]

        t1_col  = HEADER_T1 if active != 2 else INACTIVE
        t2_col  = HEADER_T2 if active != 1 else INACTIVE
        t1_surf = font_title.render("TEAM 1", True, t1_col)
        t2_surf = font_title.render("TEAM 2", True, t2_col)
        screen.blit(t1_surf, (card1_x + CARD_W // 2 - t1_surf.get_width() // 2, PADDING))
        screen.blit(t2_surf, (card2_x + CARD_W // 2 - t2_surf.get_width() // 2, PADDING))

        _draw_card(screen, font_big, 0, card1_x, card_y, active != 2)
        _draw_card(screen, font_big, 1, card2_x, card_y, active != 1)

        tip = font_small.render("Click a number to mark / unmark it", True, (127, 132, 156))
        screen.blit(tip, (WIN_W // 2 - tip.get_width() // 2, WIN_H - 20))

        pygame.display.flip()

    pygame.quit()



def start_bingo_window(card1, card2):
    global _thread
    _thread = threading.Thread(target=_pygame_loop, args=(card1, card2), daemon=False)
    _thread.start()


def set_active_team(team_number):
    with _lock:
        _state["active_team"] = team_number


def flash_number(number):
    with _lock:
        _state["highlight_number"] = int(number)


def update_cards(card1, card2):
    with _lock:
        _state["cards"][0]        = card1
        _state["cards"][1]        = card2
        _state["marked"]          = [set(), set()]
        _state["highlight_number"] = None


def stop_bingo_window():
    with _lock:
        _state["running"] = False
    if _thread is not None:
        _thread.join()