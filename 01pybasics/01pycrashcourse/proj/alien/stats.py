class GameStats:
    '''跟踪游戏统计信息的类'''

    def __init__(self, game):
        '''初始化统计信息'''
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        '''重置游戏统计信息'''
        self.ships_left = self.settings.ship_limit
