# -*- coding: utf-8 -*-
"""
    scripts.init_webhook
    ~~~~~~~~~~~~~~~~~~~~

    A simple script to manage the webhook.

    :copyright: (c) 2016 by Lujeni.
    :license: BSD, see LICENSE for more details.
"""
import argparse
import logging
import os
import sys

from trello import TrelloClient

from yaml import load


logging.basicConfig(
    level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')

logging.getLogger("requests").setLevel(logging.WARNING)


# TODO: change the way to manage the settings.
config_file = os.environ.get('MATTERLLO_CONFIG_FILE')
if not config_file:
    logging.error('Make sure the following environment variables are set: MATTERLLO_CONFIG_FILE')
    sys.exit(0)

with open(config_file, 'r') as f:
    settings = load(f)

def main():
    try:
        parser = argparse.ArgumentParser(description="Webhook helpers")
        parser.add_argument('--cleanup', dest='cleanup', action='store_true', help='delete webhook from your settings.')
        parser.add_argument('--update', dest='update', action='store_true', help='upsert webhook from your settings.')
        parser.add_argument('--init', dest='init', action='store_true', help='delete and create webhook from your settings.')

        args = parser.parse_args()
        if not args.cleanup and not args.update and not args.init:
            print parser.print_help()
            sys.exit(0)

        client = TrelloClient(api_key=settings['trello_api_key'], token=settings['trello_api_token'])
        trello_boards = client.list_boards()
        boards = settings.get('boards', [])

        # cleanup part
        if args.cleanup or args.init:
            result = [h.delete() for h in client.list_hooks()]
            logging.info('delete {} webhook'.format(len(result)))

        # update / init part
        if args.update or args.init:
            for board in trello_boards:
                if board.name in boards:
                    logging.info('try to create webhook board :: {}'.format(board.name))
                    result = client.create_hook(settings['callback_url'], board.id)
                    logging.info('create webhook board :: {} :: {}'.format(board.name, result))
    except Exception as e:
        logging.error('unable init webhook :: {}'.format(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
