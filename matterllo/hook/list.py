# -*- coding: utf-8 -*-
"""
    matterllo.hook.list
    ~~~~~~~~~~~~~~~~~~

    The application to parse list action.

    :copyright: (c) 2016 by Lujeni.
    :license: BSD, see LICENSE for more details.
"""

class Hook(object):

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
            return self.archiveList(action=action)
        return self.renameList(action)

    def archiveList(self, action):
        context = {
            'board_link': action['data']['board']['shortLink'],
            'list_name': action['data']['list']['name'],
        }
        payload = u':incoming_envelope: List archived: "[{list_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def renameList(self, action):
        context = {
            'board_link': action['data']['board']['shortLink'],
            'list_name': action['data']['list']['name'],
            'list_old_name': action['data']['old']['name'],
        }
        payload = u':incoming_envelope: List renamed from "{list_old_name}" to "[{list_name}](https://trello.com/b/{board_link})"'

        return payload.format(**context)

    def moveListFromBoard(self, action):
        context = {
            'board_target_name': action['data']['boardTarget']['name'],
            'board_name': action['data']['board']['name'],
            'board_link': action['data']['board']['shortLink'],
            'list_name': action['data']['list']['name'],
        }
        payload = u':incoming_envelope: List moved: "[{list_name}](https://trello.com/b/{board_link})" moved from "[{board_name}](https://trello.com/b/{board_link}) to board "{board_target_name}"'

        return payload.format(**context)

    def moveListToBoard(self, action):
        context = {
            'board_source_name': action['data']['boardSource']['name'],
            'board_name': action['data']['board']['name'],
            'board_link': action['data']['board']['shortLink'],
            'list_name': action['data']['list']['name'],
        }
        payload = u':incoming_envelope: List moved: "[{list_name}](https://trello.com/b/{board_link})" moved to "[{board_name}](https://trello.com/b/{board_link}) from board "{board_source_name}"'

        return payload.format(**context)
