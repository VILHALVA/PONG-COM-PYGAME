import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
DARK_GRAY = (50, 50, 50)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong Game')
clock = pygame.time.Clock()

PLAYER_WIDTH = 15
PLAYER_HEIGHT = 90
player1_x = 50
player1_y = SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
player1_speed_y = 0
player2_x = SCREEN_WIDTH - PLAYER_WIDTH - 50
player2_y = SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
player2_speed_y = 0

BALL_SIZE = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

score1 = 0
score2 = 0
font = pygame.font.SysFont(None, 55)

def draw_score():
    score_display = font.render(f"{score1} - {score2}", True, DARK_GRAY)
    screen.blit(score_display, [SCREEN_WIDTH // 2 - score_display.get_width() // 2, 10])

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2_speed_y = -5
            if event.key == pygame.K_DOWN:
                player2_speed_y = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_speed_y = 0

    player1_y += (ball_y - player1_y - PLAYER_HEIGHT // 2) * 0.05  
    player2_y += player2_speed_y

    player1_y = max(0, min(SCREEN_HEIGHT - PLAYER_HEIGHT, player1_y))
    player2_y = max(0, min(SCREEN_HEIGHT - PLAYER_HEIGHT, player2_y))
    
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
        ball_speed_y *= -1

    player1_rect = pygame.Rect(player1_x, player1_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2_rect = pygame.Rect(player2_x, player2_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE)

    if ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect):
        ball_speed_x *= -1

    if ball_x < 0:
        score2 += 1
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_speed_x *= -1
    if ball_x > SCREEN_WIDTH:
        score1 += 1
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_speed_x *= -1

    screen.fill(LIGHT_BLUE) 
    pygame.draw.rect(screen, RED, player1_rect)  
    pygame.draw.rect(screen, BLUE, player2_rect)  
    pygame.draw.ellipse(screen, WHITE, ball_rect)  
    draw_score()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
