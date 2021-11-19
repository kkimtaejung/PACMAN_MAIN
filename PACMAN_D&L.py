################################################################

# 5. 화면에 그리기

    screen.blit(background, (0, 0)) # 화면 맨 왼쪽 위를 원점으로 시작, 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos)) # 적 그리기
    screen.blit(enemy3, (enemy3_x_pos, enemy3_y_pos)) # 적 그리기
    screen.blit(enemy4, (enemy4_x_pos, enemy4_y_pos)) # 적 그리기
    screen.blit(coin, (coin_x_pos, coin_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기 ( 계속 화면을 그려줌 )

# 게임 오버&점수 메세지
game_result = "Game Over ! Final Score : %d " %i

msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
msg_rect = msg.get_rect(center=(int(screen_width /2) , int(screen_height / 2)))
screen.blit(msg, msg_rect)


pygame.display.update() # 게임화면을 다시 그리기 ( 계속 화면을 그려줌 )

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()