.. title:: settings

Configuration File Options
==========================

The following page describes the configuration options available in Matterllo.

Settings
--------

.. code-block:: yaml

    ----
    trello_api_key: ce312e17dd16abcf2d3d0fe18179a2f8

    trello_api_token: c54215580eaddbf87770276af21f7ae8e2de71b21ace631ce58534ac36264a2a

    callback_url: http://073f282a.ngrok.io

    boards:
      default_board:
        name: 'testing'
        mattermost:
          channel_one:
            subscribe: 'commentCard'
            incoming_webhook_url: 'https://gitlab.mattermost.com'
            incoming_webhook_key: 'b5g6pyoqsjy88fa6kzn7xi1rzy'
            channel: 'trello'
            username: 'Matterllo'
            icon_url: 'http://maffrigby.com/wp-content/uploads/2015/05/trello-icon.png'

          channel_two:
            subscribe: 'removeLabelFromCard addLabelToCard -commentCard'
            incoming_webhook_url: 'https://gitlab.mattermost.com'
            incoming_webhook_key: 'sw9fp5otxi8f5xafgeqwgmzfzw'
            channel: 'town-square'
            username: 'Matterllo'
            icon_url: 'http://maffrigby.com/wp-content/uploads/2015/05/trello-icon.png'

Generic
~~~~~~~
.. code-block:: yaml

    ---
    trello_api_key: ce312e17dd16abcf2d3d0fe18179a2f8

    trello_api_token: c54215580eaddbf87770276af21f7ae8e2de71b21ace631ce58534ac36264a2a

    callback_url: http://073f282a.ngrok.io


**trello_api_key**: `generate key`_

.. _generate key: http://matterllo.readthedocs.org/en/latest/requirements.html#api-key

**trello_api_token**: `generate token`_

.. _generate token: http://matterllo.readthedocs.org/en/latest/requirements.html#api-token

**callback_url**: The callback URL used by Trello to send events.

Board
~~~~~
.. code-block:: yaml

    boards:
        default_board:
            name: 'testing'
            subscribe: '*'

**name**: the name of the Trello board.

Mattermost
~~~~~~~~~~
.. note:: We use Matterhook_ library for the mattermost part.

.. note:: Matterllo support multiple channels subscription for the same trello board.

.. code-block:: yaml

    mattermost:
      channel_one:
        subscribe: '* -renameCard -archivedCard'
        incoming_webhook_url: 'https://gitlab.mattermost.com'
        incoming_webhook_key: 'b5g6pyoqsjy88fa6kzn7xi1rzy'
        channel: 'trello'
        username: 'Matterllo'
        icon_url: 'http://maffrigby.com/wp-content/uploads/2015/05/trello-icon.png'

      channel_two:
        subscribe: 'commentCard'
        incoming_webhook_url: 'https://gitlab.mattermost.com'
        incoming_webhook_key: 'b5g6pyoqsjy88fa6kzn7xi1z21'
        channel: 'trello-dev'
        username: 'Matterllo'
        icon_url: 'http://maffrigby.com/wp-content/uploads/2015/05/trello-icon.png'

.. _Matterhook: https://github.com/numberly/matterhook

**subscribe**: wich events you want to receive (default is all).
    - `*` for all events
    - `-` to remove event

 .. hlist::
   :columns: 3

    * createCard
    * updateCard
    * archivedCard
    * unarchivedCard
    * renameCard
    * renameCardDesc
    * commentCard
    * moveCardFromBoard
    * moveCardToBoard
    * updateCardDueDate
    * removeCardDueDate
    * addMemberToCard
    * remveMemberFromCard
    * addLabelToCard
    * removeLabelFromCard
    * addAttachmentToCard
    * addCheckListToCard
    * createCheckItem
    * updateCheckItemStateOnCard
    * createList
    * updateList
    * archiveList
    * renameList
    * moveListFromBoard
    * moveListToBoard

**incoming_webhook_url**: `generate webhook`_ This will probably be only your domain, since matterllo automatically appends ``/hooks/`` to it.

**incoming_webhook_key**: `generate webhook`_

.. _generate webhook: https://github.com/numberly/matterhook#getting-the-api-key

**channel**: The channel name.

.. note:: 'Town Square' became town-square.

**username**: Personalized bot username.

**icon_url**: Personalized bot icon.
