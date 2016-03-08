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
    ACTION_LIST = ['createList', 'updateList']

    def __init__(self):
        self.supported_action = self.ACTION_CARD + self.ACTION_LIST

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
        context = {
            'board_link': action['data']['board']['shortLink'],
            'list_name': action['data']['list']['name'].upper(),
            'card_name': action['data']['card']['name'],
            'card_link': action['data']['card']['shortLink'],
        }
        payload = u':incoming_envelope: New card "[{card_name}](https://trello.com/c/{card_link})" added to list "[{list_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def createList(self, action):
        context = {
            'board_name': action['data']['board']['name'],
            'board_link': action['data']['board']['shortLink'],
            'list_name': action['data']['list']['name'],
        }
        payload = u':incoming_envelope: New list "{list_name}" added to board "[{board_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def updateList(self, action):
        if action['data']['list'].get('closed', False):
            return self.archivedList(action=action)
        return self.renameList(action)

    def archivedList(self, action):
        context = {
            'board_link': action['data']['board']['shortLink'],
            'list_name': action['data']['list']['name'],
        }
        payload = u':incoming_envelope: List archived: "[{list_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def renameList(self, action):
        context = {
            'board_link': action['data']['board']['shortLink'],
            'list_name': action['data']['list']['name'].upper(),
            'list_old_name': action['data']['old']['name'].upper(),
        }
        payload = u':incoming_envelope: List renamed from "{list_old_name}" to "[{list_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)
