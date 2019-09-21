import sys, pygame

import constants


def main():
    """游戏入口， main方法"""
    # 游戏初始化
    pygame.init()
    pygame.mixer.init()

    # 创建屏幕对象
    width, height = 480, 770
    screen = pygame.display.set_mode((width, height))

    # 设置标题
    pygame.display.set_caption('飞机大战')

    # 背景图片
    bg = pygame.image.load(constants.BG_IMG)
    # 标题
    img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
    t_width, t_height = img_game_title.get_size()
    img_game_title_rect = img_game_title.get_rect()
    img_game_title_rect.left = int((width - t_width) / 2)
    img_game_title_rect.top = int((height / 2 - t_height))

    # 开始
    img_game_start = pygame.image.load(constants.IMG_GAME_START_BTN)
    s_width, s_height = img_game_start.get_size()
    img_game_start_rect = img_game_start.get_rect()
    img_game_start_rect.left = int((width - s_width) / 2)
    img_game_start_rect.top = int((height / 2 + s_height))

    # 背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load(constants.BG_MUSIC)  # 加载音乐
    pygame.mixer.music.set_volume(0.2)  # 设置音量
    pygame.mixer.music.play(-1)  # 循环播放

    # 游戏状态
    status = 0  # 0-准备中、1-游戏中、2-游戏结束

    while True:
        # 1. 监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == 0:
                    status = 1
        # 更新游戏状态
        if status == 0:
            screen.blit(bg, bg.get_rect())
            screen.blit(img_game_title, img_game_title_rect)
            screen.blit(img_game_start, img_game_start_rect)
        elif status == 1:
            screen.blit(bg, bg.get_rect())

        pygame.display.flip()


if __name__ == '__main__':
    main()