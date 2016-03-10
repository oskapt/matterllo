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
        data = action['data']
        context = {
            'board_link': data['board']['shortLink'],
            'list_name': data['list']['name'],
            'card_name': data['card']['name'],
            'card_link': data['card']['shortLink'],
        }
        payload = u':incoming_envelope: New card "[{card_name}](https://trello.com/c/{card_link})" added to list "[{list_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def updateCard(self, action):
        data = action['data']
        if data.get('listAfter') and data.get('listBefore'):
            return self.moveCardToList(action=action)

        if data['card'].get('old', False):
            return self.renameCard(action)
        if data['card'].get('closed', False):
            return self.archiveCard(action=action)
        return self.unarchiveCard(action=action)

    def archiveCard(self, action):
        data = action['data']
        context = {
            'board_link': data['board']['shortLink'],
            'card_name': data['card']['name'],
        }
        payload = u':incoming_envelope: Card archived: "[{card_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def unarchiveCard(self, action):
        data = action['data']
        context = {
            'board_link': data['board']['shortLink'],
            'card_name': data['card']['name'],
        }
        payload = u':incoming_envelope: Card unarchived: "[{card_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def renameCard(self, action):
        data = action['data']
        context = {
            'board_link': data['board']['shortLink'],
            'card_name': data['card']['name'],
            'card_old_name': data['old']['name'],
        }
        payload = u':incoming_envelope: Card renamed from "{card_old_name}" to "[{card_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def commentCard(self, action):
        data = action['data']
        context = {
            'board_link': data['board']['shortLink'],
            'card_name': data['card']['name'],
            'card_link': data['card']['shortLink'],
            'member_creator': action['memberCreator']['fullName'],
            'comment': data['text'],
        }
        payload = u''':incoming_envelope: New comment on card "[{card_name}](https://trello.com/b/{card_link})" by `{member_creator}`
> {comment}'''

        return payload.format(**context)

    def moveCardFromBoard(self, action):
        data = action['data']
        context = {
            'board_target_name': data['boardTarget']['name'],
            'board_name': data['board']['name'],
            'board_link': data['board']['shortLink'],
            'card_name': data['card']['name'],
        }
        payload = u':incoming_envelope: Card moved: "[{card_name}](https://trello.com/b/{board_link})" moved from "[{board_name}](https://trello.com/b/{board_link}) to board "{board_target_name}"'

        return payload.format(**context)

    def moveCardToBoard(self, action):
        data = action['data']
        context = {
            'board_source_name': data['boardSource']['name'],
            'board_name': data['board']['name'],
            'board_link': data['board']['shortLink'],
            'card_name': data['card']['name'],
        }
        payload = u':incoming_envelope: Card moved: "[{card_name}](https://trello.com/b/{board_link})" moved to "[{board_name}](https://trello.com/b/{board_link}) from board "{board_source_name}"'

        return payload.format(**context)
