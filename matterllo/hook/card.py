# -*- coding: utf-8 -*-
"""
    matterllo.hook.card
    ~~~~~~~~~~~~~~~~~~~

    The application to parse card action.

    :copyright: (c) 2016 by Lujeni.
    :license: BSD, see LICENSE for more details.
"""

class Hook(object):

    def createCard(self, action):
        context = {
            'board_link': action['data']['board']['shortLink'],
            'list_name': action['data']['list']['name'],
            'card_name': action['data']['card']['name'],
            'card_link': action['data']['card']['shortLink'],
        }
        payload = u':incoming_envelope: New card "[{card_name}](https://trello.com/c/{card_link})" added to list "[{list_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def updateCard(self, action):
        if action['data']['card'].get('closed', False):
            return self.archiveCard(action=action)
        return self.renameCard(action)

    def archiveCard(self, action):
        context = {
            'board_link': action['data']['board']['shortLink'],
            'card_name': action['data']['card']['name'],
        }
        payload = u':incoming_envelope: Card archived: "[{card_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def renameCard(self, action):
        context = {
            'board_link': action['data']['board']['shortLink'],
            'card_name': action['data']['card']['name'],
            'card_old_name': action['data']['old']['name'],
        }
        payload = u':incoming_envelope: Card renamed from "{card_old_name}" to "[{card_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def commentCard(self, action):
        context = {
            'board_link': action['data']['board']['shortLink'],
            'card_name': action['data']['card']['name'],
            'card_link': action['data']['card']['shortLink'],
            'member_creator': action['memberCreator']['fullName'],
            'comment': action['data']['text'],
        }
        payload = u''':incoming_envelope: New comment on card "[{card_name}](https://trello.com/b/{card_link})" by `{member_creator}`
> {comment}'''

        return payload.format(**context)
