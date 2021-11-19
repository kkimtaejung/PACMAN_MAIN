import pygame
import random

# 기본 초기화 (반드시 지정해 두어야함)
####################################################################
pygame.init() # 초기화

#화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 780 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("P A C M A N") # 게임 이름

# FPS
clock = pygame.time.Clock()
####################################################################