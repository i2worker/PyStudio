import random

class RandomWalk:
    """一个随机漫步类"""

    def __init__(self, points=5000):
        """初始化随机漫步"""
        self.points = points
        self.x = [0]
        self.y = [0]

    def fill_walk(self):
        """生成随机漫步的点"""
        while len(self.x) < self.points:
            # 生成x轴方向
            x_direction = random.choice([1, -1])
            x_distance = random.choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            # 生成y轴方向
            y_direction = random.choice([1, -1])
            y_distance = random.choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地移动
            if (x_step == 0) and (y_step == 0):
                continue

            # 计算下一个点
            next_x = self.x[-1] + x_step
            next_y = self.y[-1] + y_step

            # 存储下一个点
            self.x.append(next_x)
            self.y.append(next_y)
