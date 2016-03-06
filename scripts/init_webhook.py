# -*- coding: utf-8 -*-
"""
    scripts.init_webhook
    ~~~~~~~~~~~~~~~~~~~~

    A simple script to create the webhook.

    :copyright: (c) 2016 by Lujeni.
    :license: BSD, see LICENSE for more details.
"""
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
        client = TrelloClient(api_key=settings['trello_api_key'], token=settings['trello_api_token'])
        trello_boards = client.list_boards()
        trello_webhooks_id = [i.id_model for i in client.list_hooks()]
        boards = settings.get('boards', [])
        
        for board in trello_boards:
            if board.name in boards and board.id not in trello_webhooks_id:
                logging.info('try to create webhook board :: {}'.format(board.name))
                result = client.create_hook(settings['callback_url'], board.id)
                logging.info('create webhook board :: {} :: {}'.format(board.name, result))
    except Exception as e:
        logging.error('unable init webhook :: {}'.format(e))
        sys.exit(0)

if __name__ == '__main__':
    main()
