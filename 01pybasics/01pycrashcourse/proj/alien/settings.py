class Settings:
    '''存储游戏中所有设置的类'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.title = "Alien Invasion"
        self.fullscreen = False
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 2.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10.0
        self.fleet_direction = 1  # 1向右，-1向左
