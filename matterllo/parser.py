# -*- coding: utf-8 -*-
"""
    matterllo.parser
    ~~~~~~~~~~~~~~~~

    The application to parse each event.

    :copyright: (c) 2016 by Lujeni.
    :license: BSD, see LICENSE for more details.
"""
from matterllo.utils import logger

LOGGING = logger()


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
            LOGGING.info('action parsing not implemented :: {}'.format(e))
        except Exception as e:
            LOGGING.error('unable to parse the action :: {} :: {}'.format(e, action))

    def createCard(self, action):
        who = action['memberCreator']['fullName']
        board_name = action['data']['board']['name']
        list_name = action['data']['list']['name']
        card_name = action['data']['card']['name']
        return u'{} create card {} on {}/{}'.format(who.title(), card_name, board_name, list_name)


