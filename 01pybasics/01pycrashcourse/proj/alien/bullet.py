import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理子弹的类'''

    def __init__(self, game):
        '''创建子弹对象'''
        super().__init__()
        # 初始化子弹属性
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # 创建子弹矩形对象并设置初始位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        '''向上子弹移动'''
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self):
        '''在指定位置绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
