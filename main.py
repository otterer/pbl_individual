import argparse

from src import CoPyBot


def main(args):
    bot = CoPyBot(args)
    bot.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--slack_channel", "-sc", type=str, default="bot_test")
    args = parser.parse_args()

    main(args)
