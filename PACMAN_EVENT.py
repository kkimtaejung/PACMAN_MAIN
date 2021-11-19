##################################################################
# 2. 이벤트 처리 ( 키보드, 마우스 등 )

# 이벤트 루프 (창이 꺼지지 않게하기 위함)
cnt = 0
i = 0

running = True # 게임이 진행중인가? True = 그렇다.
while running: # True면 계속 while문 반복해라!
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정


    cnt += 1
    if cnt > 60:
        enemy_x_speed = random.randint(-5, 5)
        enemy_y_speed = random.randint(-5, 5)
        cnt = 0

    cnt += 1
    if cnt > 60:
        enemy2_x_speed = random.randint(-5, 5)
        enemy2_y_speed = random.randint(-5, 5)
        cnt = 0

    cnt += 1
    if cnt > 60:
        enemy3_x_speed = random.randint(-5, 5)
        enemy3_y_speed = random.randint(-5, 5)
        cnt = 0

    cnt += 1
    if cnt > 60:
        enemy4_x_speed = random.randint(-5, 5)
        enemy4_y_speed = random.randint(-5, 5)
        cnt = 0

    for event in pygame.event.get(): # pygame만들기 위해 무조건 적어야하는 식 ( 어떠 이벤트가 발생했는가? )
        if event.type == pygame.QUIT: # x표시로 창을 껐을 때 즉, 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 탈출

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed # to_x = to_x - 5
                character = pygame.image.load("./character_L.png")
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
                character = pygame.image.load("./character_R.png")
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
                character = pygame.image.load("./character_U.png")
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed
                character = pygame.image.load("./character_D.png")

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        # 방향키를 뗐을 때 0이 더해지기 때문에 제자리에 머문다.
#################################################################