import sys, pygame

# 初始化
pygame.init()

# 屏幕对象
screen = pygame.display.set_mode((500, 500))


class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, x, y):
        self.rect = self.rect.move(x, y)


s1 = Block((255, 0, 0), 50, 50, 50, 50)
s2 = Block((0, 255, 0), 90, 90, 100, 50)

while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(s1.image, s1.rect)
    screen.blit(s2.image, s2.rect)
    # 矩形检测碰撞
    result1 = pygame.sprite.collide_rect(s1, s2)
    # 使用缩放为一定比例的圆，检测两个小精灵之间的碰撞
    result2 = pygame.sprite.collide_circle_ratio(0.5)(s1, s2)
    print(result1, result2)  # 1 False
    pygame.display.flip()
