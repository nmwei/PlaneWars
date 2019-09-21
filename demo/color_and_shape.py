import sys, pygame

# 初始化
pygame.init()

# 屏幕对象
screen = pygame.display.set_mode((500, 500))

red = pygame.Color(255, 0, 0)

while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 直线
    pygame.draw.line(screen, red, (10, 10), (80, 80), 5)
    # 矩形
    pygame.draw.rect(screen, red, (100, 100, 50, 50), 1)
    # 圆
    pygame.draw.circle(screen, red, (300, 300), 50, 10)
    pygame.display.flip()
