import pygame
import constants


class Bullet(pygame.sprite.Sprite):
    """ 子弹类 """

    # 子弹状态
    active = True

    def __init__(self, screen, plane, speed=None):
        super().__init__()
        self.screen = screen
        # 速度
        self.speed = speed or 10
        self.plane = plane
        # 加载子弹图片
        self.image = pygame.image.load(constants.BULLET_IMG)
        # 子弹位置
        self.rect = self.image.get_rect()  # 尺寸默认为图片尺寸，位置默认为(0, 0)
        self.rect.centerx = self.plane.rect.centerx
        self.rect.top = self.plane.rect.top

        # 发射子弹的音乐效果
        self.shoot_sound = pygame.mixer.Sound(constants.BUTTON_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self, war):
        """ 更新子弹位置 """
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
        # 绘制子弹
        self.screen.blit(self.image, self.rect)
        # 碰撞检测
        targets = pygame.sprite.spritecollide(self, war.enemies, False)
        for target in targets:
            # 子弹消失
            self.kill()
            # 飞机爆炸，坠毁效果
            target.broken_down()
            # 统计游戏成绩
            war.result.score += constants.SCORE_SHOOT_SMALL
            # 保存历史记录
            war.result.set_history()



