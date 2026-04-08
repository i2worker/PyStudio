from random import randint

class Die:
    """一个骰子类"""

    def __init__(self, sides=6):
        """初始化骰子属性"""
        self.sides = sides

    def roll(self):
        """返回1到骰子面数之间的随机整数"""
        return randint(1, self.sides)
