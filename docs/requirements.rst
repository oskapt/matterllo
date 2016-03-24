.. title:: requirements

Requirements
============

Python
------
This code has been tested under Python **2.7**.

.. code-block:: bash

    # install by the setup
    Flask==0.10.1
    PyYAML==3.11
    matterhook==0.1
    py-trello==0.4.3
    python-slugify==1.2.0

.. code-block:: python

    $ pip install matterllo

Mattermost
----------
You must generate a `incoming wehbook <http://docs.mattermost.com/developer/webhooks-incoming.html#setting-up-existing-integrations>`_ and note the new webhook url.

.. code-block:: bash

    # example
    https://gitlab.mattermost.com/hook/'b5g6pyoqsjy88fa6kzn7xi1rzy

Trello
------
API key
~~~~~~~
`Here <https://trello.com/app-key>`_

.. code-block:: bash

    # example
    6bb82ec2e4a568d886896c61df59516y0

API token
~~~~~~~~~
`Here <https://developers.trello.com/authorize>`_

.. code-block:: bash

    # example
    bd83fd4fdce4ad7g02a95df77b920a7542f026d6eb71d7abdc4e1330e510861y0
