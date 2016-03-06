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

    EVENT_CARD = ['createCard']

    def __init__(self):
        self.supported_event = self.EVENT_CARD

    def __call__(self, event):
        """ Parse the event et return a pretty output.

        Args:
            event (dict): the trello event.
        """
        try:
            event_type = event['type']
            if event_type not in self.supported_event:
                raise NotImplementedError(event_type)
            
            event_parser = getattr(self, event_type)
            return event_parser(event=event)
        except NotImplementedError as e:
            logging.info('event parsing not implemented :: {}'.format(e))
        except Exception as e:
            logging.error('unable to parse the event :: {} :: {}'.format(e, event))

    def createCard(self, event):
        who = event['memberCreator']['fullName']
        board_name = event['data']['board']['name']
        list_name = event['data']['list']['name']
        card_name = event['data']['card']['name']
        return u'{} create card {} on {}/{}'.format(who.title(), card_name, board_name, list_name)
        

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
        event_result = parser(event=action)
        mwh = Webhook(settings['matter_url'], settings['matter_api_key'])
        mwh.username = settings['matter_username']
        mwh.icon_url = settings['matter_icon_url']
        
        for channel in settings['boards'][board]['channel']:
            mwh.send(event_result, channel='channel')
    except KeyError as e:
        logging.error('missing necessary field :: {} :: {}'.format(e, data))
    except Exception as e:
        logging.error('unable to handle event :: {}'.format(e))
    finally:
        # TODO: better response
        return 'ok'
