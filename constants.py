import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 静态文件目录
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# 背景图片
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
BG_OVER_IMG = os.path.join(ASSETS_DIR, 'images/game_over.png')

# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')
# 开始按钮
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')

# 游戏字体
FONT = os.path.join(ASSETS_DIR, 'font/hwxw.ttf')
# 游戏分数颜色
SCORE_COLOR = (255, 255, 0)

# 击中小型飞机分数
SCORE_SHOOT_SMALL = 10

# 背景音乐
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/game_bg_music.wav')

# 我的飞机的静态资源
MY_PLANE_IMA_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero1.png'),
    os.path.join(ASSETS_DIR, 'images/hero2.png')
]
# 我方飞机坠毁静态资源
MY_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png'),
]

# 子弹图片
BULLET_IMG = os.path.join(ASSETS_DIR, 'images/bullet1.png')
BUTTON_SHOOT_SOUND = os.path.join(ASSETS_DIR, 'sounds/bullet.wav')

# 小型敌机图片及音效
SMALL_ENEMY_PLANE_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/enemy1.png')
]
SMALL_ENEMY_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/enemy1_down1.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down2.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down3.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down4.png'),
]
# 坠毁音效
SMALL_ENEMY_PLANE_DOWN_SOUND = os.path.join(ASSETS_DIR, 'sounds/enemy1_down.wav')

# 游戏结果存储文件地址
MAX_SCORE_FILE = os.path.join(BASE_DIR, 'store/result.txt')

