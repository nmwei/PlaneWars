import sys, pygame

# 1. pygame初始化
pygame.init()

size = width, height = 320, 240  # 元组，等价于(320, 240)
speed = [2, 2]
black = 0, 0, 0  # 元组，等价于(0, 0, 0)

# 2. 创建窗口对象
screen = pygame.display.set_mode(size)
# 获取图片对象
ball = pygame.image.load("intro_ball.gif")
# 获取图片对象位置
ballrect = ball.get_rect()

# 3. 游戏主循环
while 1:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 更新游戏状态(图片对象位置)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # 窗口视图绘制
    screen.fill(black)  # 使用黑色填充窗口
    screen.blit(ball, ballrect)  # 指定位置绘制图片
    pygame.display.flip() # 更新窗口