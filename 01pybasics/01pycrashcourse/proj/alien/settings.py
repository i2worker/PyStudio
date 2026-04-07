class Settings:
    '''存储游戏中所有设置的类'''

    def __init__(self):
        '''初始化游戏的固定设置'''
        # 屏幕设置
        self.title = "Alien Invasion"
        self.fullscreen = False
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        # 外星人设置
        self.fleet_drop_speed = 10.0

        # 加速设置
        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        '''初始化游戏的动态设置'''
        self.ship_speed = 3.0
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        '''增加游戏速度'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
