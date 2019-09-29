import constants


class PlayResult(object):
    __score = 0     # 总分
    __life = 3      # 生命数量
    __blood = 10    # 生命值

    @staticmethod
    def max_score():
        """ 获取记录最高分 """
        max_score = 0
        with open(constants.MAX_SCORE_FILE, 'r') as f:
            score = f.read()
            if score:
                max_score = score
        return max_score

    @property
    def score(self):
        """ 获取游戏分数 """
        return self.__score

    @score.setter
    def score(self, value):
        """ 设置游戏分数 """
        if value < 0:
            return
        self.__score = value

    def set_history(self):
        """记录最高分"""
        if int(self.max_score()) < self.score:
            with open(constants.MAX_SCORE_FILE, 'w') as f:
                f.write('{}'.format(self.score))


