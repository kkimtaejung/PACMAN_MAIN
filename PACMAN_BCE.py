####################################################################


# 배경 이미지 불러오기
background = pygame.image.load("./background3.png")

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("./character_R.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = (screen_width /2 ) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = (screen_height /2) - (character_height / 2) # 화면 세로의 절반 크기에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1

# 적 enermy 캐릭터
enemy = pygame.image.load("./enemy1.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width =  enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width/10) - enemy_width
enemy_y_pos = (screen_height/10) - enemy_height
enemy_x_speed = random.randint(-5, 5)
enemy_y_speed = random.randint(-5, 5)

enemy2 = pygame.image.load("./enemy2.png")
enemy2_size = enemy2.get_rect().size # 이미지의 크기를 구해옴
enemy2_width =  enemy2_size[0] # 캐릭터의 가로 크기
enemy2_height = enemy2_size[1] # 캐릭터의 세로 크기
enemy2_x_pos = screen_width - enemy2_width
enemy2_y_pos = (screen_height/10) - enemy2_height
enemy2_x_speed = random.randint(-5, 5)
enemy2_y_speed = random.randint(-5, 5)

enemy3 = pygame.image.load("./enemy3.png")
enemy3_size = enemy3.get_rect().size # 이미지의 크기를 구해옴
enemy3_width =  enemy3_size[0] # 캐릭터의 가로 크기
enemy3_height = enemy3_size[1] # 캐릭터의 세로 크기
enemy3_x_pos = (screen_width/10) - enemy3_width
enemy3_y_pos = screen_height - enemy3_height
enemy3_x_speed = random.randint(-5, 5)
enemy3_y_speed = random.randint(-5, 5)

enemy4 = pygame.image.load("./enemy4.png")
enemy4_size = enemy4.get_rect().size # 이미지의 크기를 구해옴
enemy4_width =  enemy4_size[0] # 캐릭터의 가로 크기
enemy4_height = enemy4_size[1] # 캐릭터의 세로 크기
enemy4_x_pos = screen_width - enemy4_width
enemy4_y_pos = screen_height - enemy4_height
enemy4_x_speed = random.randint(-5, 5)
enemy4_y_speed = random.randint(-5, 5)

coin = pygame.image.load("./coin.png")
coin_size = coin.get_rect().size
coin_width = coin_size[0]
coin_height = coin_size[1]
coin_x_pos = random.randint(coin_width, screen_width - coin_width)
coin_y_pos = random.randint(coin_height, screen_height - coin_height)


#Font 정의
game_font = pygame.font.Font(None, 40)


#################################################################