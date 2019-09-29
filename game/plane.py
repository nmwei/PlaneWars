import random

import pygame

import constants
from game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    """
    飞机的基础类
    """
    # 飞机的图片
    plane_images = []
    # 飞机爆炸的图片
    destroy_images = []
    # 坠毁的音乐地址
    down_sound_src = None
    # 飞机的状态
    active = True
    # 飞机发射的子弹精灵组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        super().__init__()
        self.screen = screen
        #  加载静态资源
        self.img_list = []
        self.destroy_img_list = []
        self.down_sound = None
        self.load_src()
        # 飞机飞行速度
        self.speed = speed or 10
        # 飞机的位置
        self.rect = self.img_list[0].get_rect()
        self.screen_width, self.screen_height = self.screen.get_size()
        self.rect.bottom = self.screen_height
        self.rect.centerx = int(self.screen_width / 2)

    def load_src(self):
        """ 加载静态资源 """
        # 飞机图像
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))
        # 飞机坠毁图像
        for img in self.destroy_images:
            self.destroy_img_list.append(pygame.image.load(img))
        # 飞机坠毁的音乐
        if self.down_sound_src:
            # 加载特效音乐，使用Sound
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return self.img_list[0]

    def blit(self):
        """ 飞机绘制 """
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        """ 向上移动 """
        self.rect.top -= self.speed

    def move_down(self):
        """ 向下移动 """
        self.rect.top += self.speed

    def move_left(self):
        """ 向左移动 """
        self.rect.left -= self.speed

    def move_right(self):
        """ 向右移动 """
        self.rect.left += self.speed

    def broken_down(self):
        """ 飞机坠毁 """
        # 1. 播放坠毁音乐
        if self.down_sound:
            self.down_sound.play()
        # 2. 播放坠毁动画
        for img in self.destroy_img_list:
            self.screen.blit(img, self.rect)
        # 3. 修改状态
        self.active = False

    def shoot(self):
        """ 发射子弹 """
        bullet = Bullet(self.screen, self, 20)
        self.bullets.add(bullet)


class MyPlane(Plane):
    # 飞机的图片
    plane_images = constants.MY_PLANE_IMA_LIST
    # 飞机爆炸的图片
    destroy_images = constants.MY_DESTROY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = None

    def update(self, war):
        """ 刷新视图 """
        if war.frame % 5:  # 切换飞机的喷气式动画效果
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)
        # 移动
        self.move(war.keyboard)
        # 射击
        if war.frame % 3 == 0:
            self.shoot()
        # 碰撞检测
        targets = pygame.sprite.spritecollide(self, war.enemies, False)
        if targets:
            # 游戏结束
            war.status = war.OVER
            # 清除敌方飞机
            war.enemies.empty()
            war.small_enemies.empty()
            # 我方飞机坠毁效果
            self.broken_down()
            # 记录游戏成绩

    def move(self, keyboard):
        if keyboard == pygame.K_w or keyboard == pygame.K_UP:
            self.move_up()
        elif keyboard == pygame.K_s or keyboard == pygame.K_DOWN:
            self.move_down()
        elif keyboard == pygame.K_a or keyboard == pygame.K_LEFT:
            self.move_left()
        elif keyboard == pygame.K_d or keyboard == pygame.K_RIGHT:
            self.move_right()


    def move_up(self):
        """ 向上移动 """
        super().move_up()
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        """ 向下移动 """
        super().move_down()
        max_bottom = self.screen.get_height()
        if self.rect.bottom > max_bottom:
            self.rect.bottom = max_bottom

    def move_left(self):
        """ 向左移动 """
        super().move_left()
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        """ 向右移动 """
        super().move_right()
        max_right = self.screen.get_width()
        if self.rect.right > max_right:
            self.rect.right = max_right


class SmallEnemyPlane(Plane):
    # 飞机的图片
    plane_images = constants.SMALL_ENEMY_PLANE_IMG_LIST
    # 飞机爆炸的图片
    destroy_images = constants.SMALL_ENEMY_DESTROY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = constants.SMALL_ENEMY_PLANE_DOWN_SOUND

    def __init__(self, screen, speed):
        super().__init__(screen, speed)
        self.init_pos()

    def update(self, frame):
        """ 更新飞机的移动 """
        super().move_down()
        self.blit()
        if self.rect.top >= self.screen_height:
            self.active = False
            self.reset()

    def reset(self):
        """ 重置飞机的状态 """
        self.active = True
        self.init_pos()

    def init_pos(self):
        """ 初始化飞机位置 """
        self.rect.left = random.randint(0, self.screen_width - self.rect.width)
        self.rect.top = random.randint(-5 * self.rect.height, -self.rect.height)

    def broken_down(self):
        """ 飞机爆炸 """
        super().broken_down()
        # 重复利用飞机对象
        self.reset()