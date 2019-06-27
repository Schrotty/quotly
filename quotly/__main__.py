import os
import sys

from quotly.QuotyBot import quoty_bot

if __name__ == "__main__":
    token = None

    # using token from command line
    if len(sys.argv) > 0:
        token = sys.argv[0]

    # using token from .env file
    if os.path.exists('.env') and os.getenv('TOKEN') and token is not None:
        token = os.getenv('TOKEN')

    if token is not None:
        quoty_bot.run(token)
    else:
        print('> No discord bot token found!')
