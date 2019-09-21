import sys, pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.mixer.music.load('./static/bg_music.mp3')  # 加载音乐
pygame.mixer.music.set_volume(0.5)  # 设置音量(0-1)
pygame.mixer.music.play(-1)  # 循环播放

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



