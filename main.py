
from game.war import PlaneWars


def main():
    """游戏入口， main方法"""
    war = PlaneWars()
    war.add_small_enemies(6)
    war.run_game()


if __name__ == '__main__':
    main()