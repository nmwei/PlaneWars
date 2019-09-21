import sys, pygame


pygame.init()

screen = pygame.display.set_mode((500, 500))
red = pygame.Color(255, 0, 0)

# 使用指定字体
font = pygame.font.Font('./static/hwxw.ttf', 60)
text = font.render('华文新魏', True, red, (255, 255, 255)) # 文字 平滑字体 文字颜色 背景颜色

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(text, (20, 100))
    pygame.display.flip()
