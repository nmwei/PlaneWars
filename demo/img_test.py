import sys, pygame

# 初始化
pygame.init()

# 屏幕对象
screen = pygame.display.set_mode((500, 500))
# 加载图片
ball = pygame.image.load('intro_ball.gif')
# 获取图片位置
rect = ball.get_rect()

while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 绘制
    screen.blit(ball, rect)
    screen.blit(ball, rect.move([50, 50]))
    screen.blit(ball, (100, 100))
    pygame.display.flip()
