import sys
import time

import pygame

from settings import Settings
from stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self._init_windows()
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.game_active = True

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

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        '''响应键盘和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # 按下键盘
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # 松开键盘
                self._check_keyup_events(event)
            elif event.type == pygame.QUIT:  # 退出游戏
                sys.exit()

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
        '''更新子弹位置并检查碰撞事件'''
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:  # 子弹超出屏幕顶部
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        '''检查子弹与外星人之间的碰撞'''
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:  # 所有外星人都被消灭
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        '''创建外星人舰队'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - alien_height * 8):
            while current_x < (self.settings.screen_width - alien_width * 2):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x, y):
        '''创建一个外星人'''
        new_alien = Alien(self)
        new_alien.x = x
        new_alien.rect.x = x
        new_alien.rect.y = y
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        '''检查外星人舰队是否到达屏幕边缘'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''改变外星人舰队的移动方向'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        '''响应飞船和外星人的碰撞'''
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            time.sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        '''检查外星人舰队是否到达底部'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _update_aliens(self):
        '''更新外星人舰队的位置'''
        self._check_fleet_edges()
        self.aliens.update()

        # 检查外星人舰队是否与飞船碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens): # type: ignore
            self._ship_hit()

        # 检查外星人舰队是否到达底部
        self._check_aliens_bottom()

    def _update_screen(self):
        '''更新屏幕图像并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)

        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 绘制飞船
        self.ship.blitme()

        # 绘制外星人舰队
        self.aliens.draw(self.screen)

        # 更新屏幕显示
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
