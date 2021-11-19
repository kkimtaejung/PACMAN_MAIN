#################################################################

# 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리  
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width



    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    # 적 위치 정의

    enemy_x_pos += enemy_x_speed
    enemy_y_pos += enemy_y_speed

    enemy2_x_pos += enemy2_x_speed
    enemy2_y_pos += enemy2_y_speed

    enemy3_x_pos += enemy3_x_speed
    enemy3_y_pos += enemy3_y_speed

    enemy4_x_pos += enemy4_x_speed
    enemy4_y_pos += enemy4_y_speed

    
    if enemy_x_pos < 0:
        enemy_x_pos = 0
    elif enemy_x_pos > screen_width - enemy_width:
        enemy_x_pos = screen_width - enemy_width

    if enemy_y_pos < 0:
        enemy_y_pos = 0
    elif enemy_y_pos > screen_width - enemy_width:
        enemy_y_pos = screen_width - enemy_width

    if enemy2_x_pos < 0:
        enemy2_x_pos = 0
    elif enemy2_x_pos > screen_width - enemy2_width:
        enemy2_x_pos = screen_width - enemy2_width

    if enemy2_y_pos < 0:
        enemy2_y_pos = 0
    elif enemy2_y_pos > screen_width - enemy2_width:
        enemy2_y_pos = screen_width - enemy2_width

    if enemy3_x_pos < 0:
        enemy3_x_pos = 0
    elif enemy3_x_pos > screen_width - enemy3_width:
        enemy3_x_pos = screen_width - enemy3_width

    if enemy3_y_pos < 0:
        enemy3_y_pos = 0
    elif enemy3_y_pos > screen_width - enemy3_width:
        enemy3_y_pos = screen_width - enemy3_width

    if enemy4_x_pos < 0:
        enemy4_x_pos = 0
    elif enemy4_x_pos > screen_width - enemy4_width:
        enemy4_x_pos = screen_width - enemy4_width

    if enemy4_y_pos < 0:
        enemy4_y_pos = 0
    elif enemy4_y_pos > screen_width - enemy4_width:
        enemy4_y_pos = screen_width - enemy4_width


################################################################