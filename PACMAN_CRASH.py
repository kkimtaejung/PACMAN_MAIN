################################################################

# 4. 충돌 처리

    # 충돌 처리를 위한 rect 정보 업데이트

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy3_x_pos
    enemy3_rect.top = enemy3_y_pos

    enemy4_rect = enemy4.get_rect()
    enemy4_rect.left = enemy4_x_pos
    enemy4_rect.top = enemy4_y_pos
    
    coin_rect = coin.get_rect()
    coin_rect.left = coin_x_pos
    coin_rect.top = coin_y_pos

    

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
        game_result = "Game Over"

    if character_rect.colliderect(enemy2_rect):
        print("충돌했어요")
        running = False
        game_result = "Game Over"

    if character_rect.colliderect(enemy3_rect):
        print("충돌했어요")
        running = False
        game_result = "Game Over"


    if character_rect.colliderect(enemy4_rect):
        print("충돌했어요")
        running = False
        game_result = "Game Over"


    if character_rect.colliderect(coin_rect):
        print("100점 추가")
        i += 100
        coin_x_pos = random.randint(coin_width, screen_width - coin_width)
        coin_y_pos = random.randint(coin_height, screen_height - coin_height)
        screen.blit(coin, (coin_x_pos, coin_y_pos))


        


    

################################################################