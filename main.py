import pygame
import sys

from player import Player
from ball import Ball

# 초기화
pygame.init()

# 화면 설정
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avoid the Falling Balls")

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)

# 점수 초기화
score = 0
font = pygame.font.SysFont(None, 36)

# 배경 음악 및 효과음
# pygame.mixer.music.load('assets/background_music.mp3')
# pygame.mixer.music.play(-1)  # 무한 반복
# hit_sound = pygame.mixer.Sound('assets/hit_sound.wav')
# game_over_sound = pygame.mixer.Sound('assets/game_over_sound.wav')

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()

# 플레이어 생성
player = Player()
all_sprites.add(player)

# 공 생성 함수
def create_ball():
    ball = Ball()
    all_sprites.add(ball)
    balls.add(ball)

# 난이도 설정
difficulty_increase_timer = pygame.USEREVENT + 1
pygame.time.set_timer(difficulty_increase_timer, 1000)  # 10초마다 난이도 증가

# 초기 공 생성
for _ in range(10):
    create_ball()

# 메인 루프
clock = pygame.time.Clock()
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == difficulty_increase_timer:
            create_ball()

    if not game_over:
        # 업데이트
        all_sprites.update()

        # 충돌 감지
        if pygame.sprite.spritecollideany(player, balls):
            # hit_sound.play()
            # game_over_sound.play()
            game_over = True
            pygame.mixer.music.stop()

        # 화면 그리기
        screen.fill(black)
        all_sprites.draw(screen)

        # 점수 표시
        score += 1
        score_text = font.render(f'Score: {score}', True, white)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        # 프레임 속도 조절
        clock.tick(60)
    else:
        # 게임 오버 화면
        screen.fill(black)
        game_over_text = font.render('Game Over! Press R to Restart', True, white)
        final_score_text = font.render(f'Final Score: {score}', True, white)
        screen.blit(game_over_text, (200, 250))
        screen.blit(final_score_text, (300, 300))
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            score = 0
            # pygame.mixer.music.play(-1)
            all_sprites.empty()
            balls.empty()
            all_sprites.add(player)
            for _ in range(10):
                create_ball()

pygame.quit()
sys.exit()
