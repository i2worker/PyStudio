import pygame

class Ship():
    '''管理飞船的类'''

    def __init__(self, game):
        '''初始化飞船并设置其初始位置'''
        # 初始化飞船属性
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        # 加载飞船图像，设置初始位置为屏幕底部居中
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # 飞船移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据飞船移动标志调整位置'''
        # 向右移动飞船
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # 向左移动飞船
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 更新矩形对象的位置
        self.rect.x = int(self.x)

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''将飞船居中显示'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
