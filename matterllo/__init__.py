# -*- coding: utf-8 -*-
"""
    matterllo
    ~~~~~~~~~

    The core application.

    :copyright: (c) 2016 by Lujeni.
    :license: BSD, see LICENSE for more details.
"""
import logging
import os
import sys


from matterhook import Webhook

from flask import Flask
from flask import request

from yaml import load


logging.basicConfig(
    level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')


# TODO: change the way to manage the settings.
config_file = os.environ.get('MATTERLLO_CONFIG_FILE')
if not config_file:
    logging.error('Make sure the following environment variables are set: MATTERLLO_CONFIG_FILE')
    sys.exit(0)

with open(config_file, 'r') as f:
    settings = load(f)


app = Flask(__name__)


class Parser(object):

    ACTION_CARD = ['createCard']

    def __init__(self):
        self.supported_action = self.ACTION_CARD

    def __call__(self, action):
        """ Parse the event/action and return a pretty output.

        Args:
            action (dict): the trello action data.
        """
        try:
            action_type = action['type']
            if action_type not in self.supported_action:
                raise NotImplementedError(action_type)

            action_parser = getattr(self, action_type)
            return action_parser(action=action)
        except NotImplementedError as e:
            logging.info('action parsing not implemented :: {}'.format(e))
        except Exception as e:
            logging.error('unable to parse the action :: {} :: {}'.format(e, action))

    def createCard(self, action):
        who = action['memberCreator']['fullName']
        board_name = action['data']['board']['name']
        list_name = action['data']['list']['name']
        card_name = action['data']['card']['name']
        return u'{} create card {} on {}/{}'.format(who.title(), card_name, board_name, list_name)


class Send(object):

    def __init__(self, board, action, payload):
        """ Init the necessary stuff to sent the event.

        Args:
            board (str): the name board.
            action (dict): the trello action data.
            payload (str): the event payload.
        """
        self.board = board
        self.action = action
        self.payload = payload

    def __call__(self):
        try:
            for key, values  in settings.get('boards', {}).items():
                logging.info('{} :: {}'.format(self.board, values['name']))
                if self.board != values['name']:
                    continue
                
                if self.action['type'] not in values['subscribe'] and values['subscribe'] != '*':
                    logging.info('{} :: no subscribe for this event :: {}'.format(key, self.action['type']))
                    continue

                mwh = Webhook(values['incoming_webhook_url'],
                              values['incoming_webhook_key'])
                mwh.username = values['username']
                mwh.icon_url = values['icon_url']
                mwh.send(self.payload, channel=values['channel'])
        except Exception as e:
            logging.error('unable to send payload :: {}'.format(e))


@app.route('/trelloCallbacks/', methods=['GET', 'POST'])
def callback():
    try:
        if request.method != 'POST':
            return 'ok'

        data = request.json
        action = data['action']
        board = data['model']['name']

        # NOTE: it's ugly to init for each request the parser class
        parser = Parser()
        payload = parser(action=action)

        if payload:
            send = Send(board=board, action=action, payload=payload)
            send()
    except KeyError as e:
        logging.error('missing necessary field :: {} :: {}'.format(e, data))
    except Exception as e:
        logging.error('unable to handle event :: {}'.format(e))
    finally:
        # TODO: better response
        return 'ok'
