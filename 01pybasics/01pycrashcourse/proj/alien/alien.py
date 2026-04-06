import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.settings = Settings()
        self._init_windows()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

    def _init_windows(self):
        '''初始化游戏窗口'''
        if self.settings.fullscreen:  # 全屏模式
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:  # 窗口模式
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.title)

    def run_game(self):
        '''开始游戏主循环'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        '''响应键盘和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 退出游戏
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 按下键盘
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # 松开键盘
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''响应按下键盘事件'''
        if event.key == pygame.K_RIGHT:  # 右移飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # 左移飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:  # 发射子弹
            self._fire_bullet()
        elif event.key == pygame.K_q:  # 按Q退出游戏
            sys.exit()

    def _check_keyup_events(self, event):
        '''响应松开键盘事件'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''创建一颗子弹并将其加入到子弹组中'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''更新子弹位置并删除已消失的子弹'''
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        '''更新屏幕图像并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():  # 绘制子弹
            bullet.draw_bullet()

        self.ship.blitme()  # 绘制飞船

        pygame.display.flip()  # 更新屏幕显示


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
