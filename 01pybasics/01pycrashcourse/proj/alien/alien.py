import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    '''管理外星人的类'''

    def __init__(self, game):
        '''初始化外星人类'''
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # 加载外星人图像并设置其初始位置
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def update(self):
        '''移动外星人'''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = int(self.x)

    def check_edges(self):
        '''检查外星人是否到达屏幕边缘'''
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
