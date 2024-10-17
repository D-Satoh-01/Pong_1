import pygame, sys, random, time, os

pygame.mixer.init()

run = False
start_menu = True
pause = False
gameover = False
stage = 1
ball_speed_x = 4
ball_speed_y = 4
player_paddle_1_speed = 0
player_paddle_2_speed = 0
player_paddle_3_speed = 0
cpu_paddle_1_speed = 2
cpu_paddle_2_speed = 2
cpu_paddle_3_speed = 2
cpu_points, player_points = 0, 0
bound_sound = pygame.mixer.Sound("Sounds/sound_1.mp3")

def reset_ball():
    global pause, ball_speed_x, ball_speed_y, stage, cpu_paddle_1_speed, cpu_paddle_2_speed, cpu_paddle_3_speed
    
    if stage == 1:
        ball_speed_x = 4
        ball_speed_y = 4
    if stage == 2:
        ball_speed_x = 4
        ball_speed_y = 4
    if stage == 3:
        ball_speed_x = 5
        ball_speed_y = 5
    if stage == 4:
        ball_speed_x = 5
        ball_speed_y = 5
    if stage == 5:
        ball_speed_x = 6
        ball_speed_y = 6
    if stage == 6:
        ball_speed_x = 6
        ball_speed_y = 6
    if stage == 7:
        ball_speed_x = 7
        ball_speed_y = 7
    if stage == 8:
        ball_speed_x = 7
        ball_speed_y = 7
    if stage == 9:
        ball_speed_x = 8
        ball_speed_y = 8
    if stage == 10:
        ball_speed_x = 7
        ball_speed_y = 7

    ball.x = screen_width/2 - 10
    ball.y = random.randint(10,100)
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1])
    pause = True

def point_won(winner):
    global cpu_points, player_points, ball_speed_x, ball_speed_y, pause, gameover, stage, run

    if winner == "player":
        player_points += 1
        ball_speed_x = 0
        ball_speed_y = 0
        pause = True
        if player_points == 3:
            stage += 1
            player_points = 0
            cpu_points = 0

    if winner == "cpu":
        cpu_points += 1
        ball_speed_x = 0
        ball_speed_y = 0
        pause = True
        if cpu_points == 3:
            player_points = 0
            cpu_points = 0
            stage = 1
            run = False
            gameover = True
            
    reset_ball()

def animate_ball():
    global ball_speed_x, ball_speed_y, pause
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1
        
    # ボールが画面外に行ったらリセット
    if ball.top < - 5:
        reset_ball
    if ball.bottom > screen_height + 5:
        reset_ball

    if ball.right >= screen_width:
        point_won("cpu")

    if ball.left <= 0:
        point_won("player")

    if ball.colliderect(player_paddle_1) or ball.colliderect(cpu_paddle_1):
        ball_speed_x *= -1.05
        bound_sound.play()
        bound_sound.set_volume(0.1)
        if ball_speed_y > 0:
            ball_speed_y += ball_speed_y * -0.5 -0.5
        if ball_speed_y < 0:
            ball_speed_y += ball_speed_y * 0.5 -0.5
    if ball.colliderect(player_paddle_2) or ball.colliderect(cpu_paddle_2):
        ball_speed_x *= -1.3
        bound_sound.play()
        bound_sound.set_volume(0.1)
    if ball.colliderect(player_paddle_3) or ball.colliderect(cpu_paddle_3):
        ball_speed_x *= -1.05
        bound_sound.play()
        bound_sound.set_volume(0.1)
        if ball_speed_y > 0:
            ball_speed_y += ball_speed_y * 0.5 + 0.5
        if ball_speed_y < 0:
            ball_speed_y += ball_speed_y * 0.5 + 0.5
            
    # ボールのスピード制限
    if ball_speed_x > 7:
        ball_speed_x = 7
    if ball_speed_y > 7:
        ball_speed_y = 7
    if ball_speed_x > 10:
        reset_ball
    if ball_speed_y > 10:
        reset_ball

def animate_player():
    global player_paddle_1_speed, player_paddle_2_speed, player_paddle_3_speed
    player_paddle_1.y += player_paddle_1_speed
    player_paddle_2.y += player_paddle_2_speed
    player_paddle_3.y += player_paddle_3_speed

    if player_paddle_1.top <= 0:
        player_paddle_1.top = 0 - 5
        player_paddle_2_speed = 0
        player_paddle_3_speed = 0

    if player_paddle_3.bottom >= screen_height:
        player_paddle_3.bottom = screen_height + 5
        player_paddle_1_speed = 0
        player_paddle_2_speed = 0

def animate_cpu():
    global cpu_paddle_1_speed, cpu_paddle_2_speed, cpu_paddle_3_speed
    cpu_paddle_1.y += cpu_paddle_1_speed
    cpu_paddle_2.y += cpu_paddle_2_speed
    cpu_paddle_3.y += cpu_paddle_3_speed

    if ball.centery <= cpu_paddle_2.centery and stage == 1:
        cpu_paddle_1_speed = -4
        cpu_paddle_2_speed = -4
        cpu_paddle_3_speed = -4
    if ball.centery >= cpu_paddle_2.centery and stage == 1:
        cpu_paddle_1_speed = 4
        cpu_paddle_2_speed = 4
        cpu_paddle_3_speed = 4
    if ball.centery <= cpu_paddle_2.centery and stage == 2:
        cpu_paddle_1_speed = -5
        cpu_paddle_2_speed = -5
        cpu_paddle_3_speed = -5
    if ball.centery >= cpu_paddle_2.centery and stage == 2:
        cpu_paddle_1_speed = 5
        cpu_paddle_2_speed = 5
        cpu_paddle_3_speed = 5
    if ball.centery <= cpu_paddle_2.centery and stage == 3:
        cpu_paddle_1_speed = -5
        cpu_paddle_2_speed = -5
        cpu_paddle_3_speed = -5
    if ball.centery >= cpu_paddle_2.centery and stage == 3:
        cpu_paddle_1_speed = 5
        cpu_paddle_2_speed = 5
        cpu_paddle_3_speed = 5
    if ball.centery <= cpu_paddle_2.centery and stage == 4:
        cpu_paddle_1_speed = -6
        cpu_paddle_2_speed = -6
        cpu_paddle_3_speed = -6
    if ball.centery >= cpu_paddle_2.centery and stage == 4:
        cpu_paddle_1_speed = 6
        cpu_paddle_2_speed = 6
        cpu_paddle_3_speed = 6
    if ball.centery <= cpu_paddle_2.centery and stage == 5:
        cpu_paddle_1_speed = -6
        cpu_paddle_2_speed = -6
        cpu_paddle_3_speed = -6
    if ball.centery >= cpu_paddle_2.centery and stage == 5:
        cpu_paddle_1_speed = 6
        cpu_paddle_2_speed = 6
        cpu_paddle_3_speed = 6
    if ball.centery <= cpu_paddle_2.centery and stage == 6:
        cpu_paddle_1_speed = -7
        cpu_paddle_2_speed = -7
        cpu_paddle_3_speed = -7
    if ball.centery >= cpu_paddle_2.centery and stage == 6:
        cpu_paddle_1_speed = 7
        cpu_paddle_2_speed = 7
        cpu_paddle_3_speed = 7
    if ball.centery <= cpu_paddle_2.centery and stage == 7:
        cpu_paddle_1_speed = -7
        cpu_paddle_2_speed = -7
        cpu_paddle_3_speed = -7
    if ball.centery >= cpu_paddle_2.centery and stage == 7:
        cpu_paddle_1_speed = 7
        cpu_paddle_2_speed = 7
        cpu_paddle_3_speed = 7
    if ball.centery <= cpu_paddle_2.centery and stage == 8:
        cpu_paddle_1_speed = -8
        cpu_paddle_2_speed = -8
        cpu_paddle_3_speed = -8
    if ball.centery >= cpu_paddle_2.centery and stage == 8:
        cpu_paddle_1_speed = 8
        cpu_paddle_2_speed = 8
        cpu_paddle_3_speed = 8
    if ball.centery <= cpu_paddle_2.centery and stage == 9:
        cpu_paddle_1_speed = -8
        cpu_paddle_2_speed = -8
        cpu_paddle_3_speed = -8
    if ball.centery >= cpu_paddle_2.centery and stage == 9:
        cpu_paddle_1_speed = 8
        cpu_paddle_2_speed = 8
        cpu_paddle_3_speed = 8
    if ball.centery <= cpu_paddle_2.centery and stage >= 10:
        cpu_paddle_1_speed = -9
        cpu_paddle_2_speed = -9
        cpu_paddle_3_speed = -9
    if ball.centery >= cpu_paddle_2.centery and stage >= 10:
        cpu_paddle_1_speed = 9
        cpu_paddle_2_speed = 9
        cpu_paddle_3_speed = 9

    #if cpu_paddle_1.top <= 0:
        #cpu_paddle_1.top = 0 - 5
        #cpu_paddle_2_speed = 0
        #cpu_paddle_3_speed = 0
    #if cpu_paddle_3.bottom >= screen_height:
        #cpu_paddle_3.bottom = screen_height + 5
        #cpu_paddle_1_speed = 0
        #cpu_paddle_2_speed = 0

pygame.init()

font_1 = pygame.font.Font(None, 100)
font_2 = pygame.font.Font(None, 50)

screen_width = 1280
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

ball = pygame.Rect(0,0,30,30)
ball.center = (screen_width/2, screen_height/2)

player_paddle_1 = pygame.Rect(0,0,20,70)
player_paddle_1.midright = (screen_width - 50, screen_height/2 - 75)
player_paddle_2 = pygame.Rect(0,0,20,70)
player_paddle_2.midright = (screen_width - 50, screen_height/2)
player_paddle_3 = pygame.Rect(0,0,20,70)
player_paddle_3.midright = (screen_width - 50, screen_height/2 + 75)

cpu_paddle_1 = pygame.Rect(50,0,20,70)
cpu_paddle_1.centery = screen_height/2 - 75
cpu_paddle_2 = pygame.Rect(50,0,20,70)
cpu_paddle_2.centery = screen_height/2
cpu_paddle_3 = pygame.Rect(50,0,20,70)
cpu_paddle_3.centery = screen_height/2 + 75

while True:
    #Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and run == False and start_menu == True:
            start_menu = False
            run = True
        
        if keys[pygame.K_SPACE] and pause == True:
            reset_ball()
            pause = False
        
        if keys[pygame.K_SPACE] and gameover == True:
            reset_ball()
            gameover = False
            time.sleep(1)
            start_menu = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_paddle_1_speed = -6
                player_paddle_2_speed = -6
                player_paddle_3_speed = -6
            if event.key == pygame.K_DOWN:
                player_paddle_1_speed = 6
                player_paddle_2_speed = 6
                player_paddle_3_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_paddle_1_speed = 0
                player_paddle_2_speed = 0
                player_paddle_3_speed = 0
            if event.key == pygame.K_DOWN:
                player_paddle_1_speed = 0
                player_paddle_2_speed = 0
                player_paddle_3_speed = 0

    #Change the positions of the game objects
    if run == True:
        animate_player()
        animate_cpu()
    if run == True and pause == False and start_menu == False and gameover == False:
        animate_ball()
        
    #Clear the screen
    screen.fill('black')

    #Drawing
    pygame.draw.aaline(screen,(50,50,50),(screen_width/2, 0), (screen_width/2, screen_height))
    
    if start_menu == True:
        start_sruface = font_2.render("Press  [Space]  to  Start", True, "white")
        screen.blit(start_sruface,(screen_width/3, screen_height/2))
        
    if gameover == True:
        gameover_sruface = font_2.render("Game Over", True, "white")
        screen.blit(gameover_sruface,(screen_width/3 + 110, screen_height/2))
        gameover_sruface = font_2.render("Press  [SPACE]  to Restart", True, "white")
        screen.blit(gameover_sruface,(screen_width/3, screen_height/2 + 60))
        
    cpu_score_surface = font_1.render(str(cpu_points), True, "white")
    screen.blit(cpu_score_surface,(screen_width/4,20))
    player_score_surface = font_1.render(str(player_points), True, "white")
    screen.blit(player_score_surface,(3*screen_width/4,20))
    
    stage_surface = font_1.render(f"Stage {stage}", True, "white")
    screen.blit(stage_surface, (screen_width/3 + 100, screen_height - 200))

    #Draw the game objects
    pygame.draw.ellipse(screen,'white',ball)
    pygame.draw.rect(screen,'white',player_paddle_1)
    pygame.draw.rect(screen,'white',player_paddle_2)
    pygame.draw.rect(screen,'white',player_paddle_3)
    pygame.draw.rect(screen,'white',cpu_paddle_1)
    pygame.draw.rect(screen,'white',cpu_paddle_2)
    pygame.draw.rect(screen,'white',cpu_paddle_3)

    #Update the display
    pygame.display.update()
    clock.tick(60)