import pygame
import sys
import constants
from game.plane import MyPlane, SmallEnemyPlane
from store.result import PlayResult


class PlaneWars(object):
    """ 飞机大战类 """
    # 标题图片
    title_img = pygame.image.load(constants.IMG_GAME_TITLE)
    # 开始按钮图片
    start_img = pygame.image.load(constants.IMG_GAME_START_BTN)
    # 背景图片
    bg_img = pygame.image.load(constants.BG_IMG)
    bg_over_img = pygame.image.load(constants.BG_OVER_IMG)

    @staticmethod
    def set_game_title():
        pygame.display.set_caption('飞机大战')

    @staticmethod
    def set_bg_music():
        pygame.mixer.init()
        pygame.mixer.music.load(constants.BG_MUSIC)  # 加载音乐
        pygame.mixer.music.set_volume(0.2)  # 设置音量
        pygame.mixer.music.play(-1)  # 循环播放

    # 游戏状态: 0-准备中、1-游戏中、2-游戏结束
    READY = 0
    PLAYING = 1
    OVER = 2

    # clock对象用来追踪时间
    clock = pygame.time.Clock()

    def __init__(self):
        pygame.init()
        # 初始化屏幕对象
        self.__screen = pygame.display.set_mode((480, 770))
        # 标题位置
        self.__title_rect = self.__get_title_rect()
        # 开始按钮位置
        self.__start_rect = self.__get_start_rect()
        # 游戏状态
        self.status = self.READY
        # 初始化我的飞机
        self.__my_plane = MyPlane(self.__screen, speed=20)
        # 小型敌机(精灵组)
        self.small_enemies = pygame.sprite.Group()
        # 所有敌机(精灵组)
        self.enemies = pygame.sprite.Group()
        self.frame = 0  # 视图一共刷新了多少次
        # 游戏标题
        self.set_game_title()
        # 设置背景音乐
        self.set_bg_music()
        # 游戏字体
        self.font = pygame.font.Font(constants.FONT, 32)
        # 游戏结果
        self.result = PlayResult()
        # 按的哪个键
        self.keyboard = None

    def run_game(self):
        """ 游戏主循环 """
        while True:
            self.__add_frame()
            self.__bind_event()
            # 更新游戏状态
            if self.status == self.READY:
                # 绘制背景
                self.__screen.blit(self.bg_img, self.bg_img.get_rect())
                # 绘制游戏标题
                self.__screen.blit(self.title_img, self.__title_rect)
                # 绘制开始按钮
                self.__screen.blit(self.start_img, self.__start_rect)
            elif self.status == self.PLAYING:
                # 绘制背景
                self.__screen.blit(self.bg_img, self.bg_img.get_rect())
                # 绘制我的飞机
                self.__my_plane.update(self)
                # 绘制子弹(执行精灵组的XXX方法会调用组内每个精灵的XXX方法)
                self.__my_plane.bullets.update(self)
                # 绘制敌方飞机
                self.enemies.update(self.frame)
                # 绘制分数
                self.blit_score()
            elif self.status == self.OVER:
                # 绘制背景
                self.__screen.blit(self.bg_over_img, self.bg_over_img.get_rect())
                # 绘制本地总分
                self.blit_over_score()
                # 绘制游戏最高分
                self.blit_max_score()
            # 刷新视图
            pygame.display.flip()

    def blit_max_score(self):
        """ 绘制游戏最高分 """
        score_text = self.font.render(
            "最高分: {}".format(self.result.max_score()),
            False,
            constants.SCORE_COLOR
        )
        self.__screen.blit(score_text, (150, 40))

    def blit_over_score(self):
        """绘制游戏结束时得分"""
        score_text = self.font.render(
            "本次得分: {}".format(self.result.score),
            False,
            constants.SCORE_COLOR
        )
        score_rect = score_text.get_rect()
        width, height = self.__screen.get_size()
        score_rect.centerx = int(width / 2)
        score_rect.centery = int(height / 2)
        self.__screen.blit(score_text, score_rect)

    def blit_score(self):
        """绘制游戏运行时得分"""
        score_text = self.font.render(
            "得分: {}".format(self.result.score),
            False,
            constants.SCORE_COLOR
        )
        self.__screen.blit(score_text, score_text.get_rect())

    def add_small_enemies(self, num):
        """ 添加小型敌机 """
        for i in range(num):
            plane = SmallEnemyPlane(self.__screen, 8)
            plane.add(self.small_enemies, self.enemies)

    def __get_title_rect(self):
        """ 获取标题图片的位置信息 """
        rect = self.title_img.get_rect()
        width, height = self.__screen.get_size()
        rect.centerx = int(width / 2)
        rect.bottom = int(height / 2)
        return rect

    def __get_start_rect(self):
        """ 获取开始按钮的位置信息 """
        rect = self.start_img.get_rect()
        width, height = self.__screen.get_size()
        rect.centerx = int(width / 2)
        rect.top = int(height / 2) + 30
        return rect

    def __add_frame(self):
        # 设置帧速率
        self.clock.tick(60)
        self.frame += 1
        if self.frame >= 60:
            self.frame = 0

    def __bind_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击关闭按钮事件
                pygame.quit()
                sys.exit()
            elif self.status == self.READY:
                if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击事件
                    self.status = self.PLAYING
            elif self.status == self.PLAYING:
                if event.type == pygame.KEYDOWN:  # 键盘按下事件
                    self.keyboard = event.key
                elif event.type == pygame.KEYUP:
                    self.keyboard = None

            elif self.status == self.OVER:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.status = self.READY
                    self.add_small_enemies(6)


