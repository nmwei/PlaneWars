import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 静态文件目录
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# 背景图片
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
BG_IMG_READY = os.path.join(ASSETS_DIR, 'images/background.png')
# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')
# 开始按钮
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')


# 背景音乐
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/game_bg_music.wav')