import sys, pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

hero1 = pygame.image.load('./static/hero1.png')
hero2 = pygame.image.load('./static/hero2.png')
clock = pygame.time.Clock()

count = 1
while True:
    clock.tick(60)  # 设置动画帧数
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    # 等价写法: screen.fill(pygame.Color(255, 255, 255))
    if count % 2 == 0:
        screen.blit(hero1, (100, 100))
    else:
        screen.blit(hero2, (100, 100))
    count += 1
    pygame.display.flip()


