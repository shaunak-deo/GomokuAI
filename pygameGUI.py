import time
import pygame
from gomoku import GomokuState
import gomoku as gm
from policies.GomukuAI import Submission
import webbrowser

# Initialize Pygame environment
pygame.init()

# Define game board and visual settings
BOARD_SIZE = 15
WIN_STREAK = 5
TILE_SIZE = 40
BOARD_COLOR = (245, 245, 220)  # Beige
LINE_COLOR = (0, 0, 0)  # Black
PLAYER_COLOR = (0, 0, 0)  # Black
AI_COLOR = (255, 165, 0)  # Orange
START_BUTTON_COLOR = (0, 0, 255)  # Blue
HOVER_COLOR = (0, 0, 150)  # Dark Blue
WINDOW_DIMENSIONS = TILE_SIZE * BOARD_SIZE
FONT_COLOR = (0, 0, 0)

# Load and resize game logo
logo = pygame.image.load('logo.png')
logo_size = (400, 400)
logo = pygame.transform.scale(logo, logo_size)
start_logo_position = logo.get_rect(center=(WINDOW_DIMENSIONS / 2, WINDOW_DIMENSIONS / 3 + 50))
end_logo_position = start_logo_position  # Reuse the start logo position for consistency

# Configure Pygame window
window = pygame.display.set_mode((WINDOW_DIMENSIONS, WINDOW_DIMENSIONS))
pygame.display.set_caption('Gomoku AI Challenge')
font = pygame.font.Font(None, 36)

class GameButton:
    """Represents a button in the game interface."""
    def __init__(self, image_path, position, dimensions):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, dimensions)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
    
    def render(self, target):
        """Draws the button onto the target surface."""
        target.blit(self.image, self.rect)

    def is_clicked(self, position):
        """Checks if the button is clicked based on the given position."""
        return self.rect.collidepoint(position)

# Initialize AI policy and game state
ai_policy = Submission(BOARD_SIZE, WIN_STREAK)
game_state = GomokuState.blank(BOARD_SIZE, WIN_STREAK)

# Game control variables
is_game_active = False
game_winner = None

# Create the start button
start_button = GameButton('START.png', (WINDOW_DIMENSIONS / 2 - 100, WINDOW_DIMENSIONS / 2 + 100), (200, 200))

def draw_game_board():
    """Fills the screen with the board and draws grid lines."""
    window.fill(BOARD_COLOR)
    for i in range(BOARD_SIZE):
        pygame.draw.line(window, LINE_COLOR, (TILE_SIZE // 2, TILE_SIZE // 2 + i * TILE_SIZE),
                         (WINDOW_DIMENSIONS - TILE_SIZE // 2, TILE_SIZE // 2 + i * TILE_SIZE), 2)
        pygame.draw.line(window, LINE_COLOR, (TILE_SIZE // 2 + i * TILE_SIZE, TILE_SIZE // 2),
                         (TILE_SIZE // 2 + i * TILE_SIZE, WINDOW_DIMENSIONS - TILE_SIZE // 2), 2)

def place_game_piece(x, y, color):
    """Places a game piece on the board."""
    center = (TILE_SIZE // 2 + x * TILE_SIZE, TILE_SIZE // 2 + y * TILE_SIZE)
    pygame.draw.circle(window, color, center, TILE_SIZE // 3)

def display_start_interface():
    """Renders the start screen interface."""
    window.fill(BOARD_COLOR)
    window.blit(logo, start_logo_position)
    start_button.render(window)

def flicker_last_move(x, y):
    """Creates a flickering effect on the last move to highlight it."""
    original_color = AI_COLOR if game_state.current_player() == gm.MIN else PLAYER_COLOR
    alternate_color = (255, 255, 255)  # Use white for the flicker effect
    for _ in range(4):  # Alternate colors to create the flickering effect
        place_game_piece(x, y, alternate_color)
        pygame.display.flip()
        time.sleep(0.25)
        place_game_piece(x, y, original_color)
        pygame.display.flip()
        time.sleep(0.25)

def announce_winner(winner):
    """Displays the game winner, performs flicker effect, and resets the game interface."""
    global last_move
    display_winner_message(winner)
    window.fill(BOARD_COLOR)
    window.blit(logo, end_logo_position)
    start_button.render(window)
    global is_game_active
    is_game_active = False




def display_winner_message(winner):
    """Shows a splash screen with the winner announcement."""
    window.fill(BOARD_COLOR)
    message = f"{winner} wins!"
    text_surface = font.render(message, True, FONT_COLOR)
    text_position = text_surface.get_rect(center=(WINDOW_DIMENSIONS / 2, WINDOW_DIMENSIONS / 2))
    window.blit(text_surface, text_position)
    time.sleep(2)  # Display the message for a brief period
    pygame.display.flip()

def reset_game():
    """Resets the game to its initial state."""
    global game_state, is_game_active, game_winner
    game_state = GomokuState.blank(BOARD_SIZE, WIN_STREAK)
    is_game_active = True
    game_winner = None
    draw_game_board()

def execute_move(x, y, player):
    """Processes a move made by a player or the AI."""
    global game_state, game_winner, last_move
    game_state = game_state.perform((x, y))
    color = PLAYER_COLOR if player == gm.MAX else AI_COLOR
    place_game_piece(x, y, color)
    last_move = (x, y)

def handle_mouse_click(position):
    """Handles mouse click events during the game."""
    global is_game_active, game_winner, last_move
    if is_game_active:
        x, y = position[0] // TILE_SIZE, position[1] // TILE_SIZE
        if game_state.board[0, x, y] == 1:
            execute_move(x, y, gm.MAX)
            pygame.display.flip()
            if not game_state.is_game_over():
                ai_move = ai_policy(game_state)
                if ai_move:
                    time.sleep(0.5)
                    execute_move(*ai_move, gm.MIN)
                    pygame.display.flip()
            if game_state.is_game_over():
                game_winner = 'Player' if game_state.current_score() > 0 else 'AI'
                flicker_last_move(*last_move)  # Highlight the last move
                is_game_active = False
                display_winner_message(game_winner)

display_start_interface()

# Main game loop
is_game_active = None  # Use None to indicate the game hasn't started
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if is_game_active is False and start_button.is_clicked(pos):
                reset_game()
            elif is_game_active is None and start_button.is_clicked(pos):
                reset_game()
            elif is_game_active:
                handle_mouse_click(pos)
    if is_game_active is None:
        display_start_interface()
    elif is_game_active is False:
        announce_winner(game_winner)
    pygame.display.flip()
