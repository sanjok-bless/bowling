import logging

from game.game import Game


if __name__ == '__main__':
    try:
        Game().run()
    except KeyboardInterrupt as e:
        logging.info('Exit from run_game.py')
