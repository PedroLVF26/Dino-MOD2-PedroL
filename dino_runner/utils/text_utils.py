import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


FONT_COLOR = (255, 255, 255)
FONT_SIZE = 22
FONT_STYLE = r"C:\Users\pedro\OneDrive\Área de Trabalho\scripts-python\Dino-MOD2-PedroL\dino_runner\assets\Other\blasphemous.ttf"

def draw_message_component(
    message,
    screen,
    font_color=FONT_COLOR,
    font_size=FONT_SIZE,
    pos_y_center=SCREEN_HEIGHT // 2,
    pos_x_center=SCREEN_WIDTH // 2
):
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)
    