.. title:: usage

First Steps with Matterllo
==========================
This document is meant to give a tutorial-like overview of all common tasks while using Matterllo.

Install / Requirements
----------------------
`Here <http://matterllo.readthedocs.org/en/latest/requirements.html>`_

Generate your config file
-------------------------
`Here <http://matterllo.readthedocs.org/en/latest/settings.html>`_

Change interface or port
------------------------
You can change the network interface which Matterllo is listening on by setting
``MATTERLLO_API_HOST`` and the port by setting ``MATTERLLO_API_PORT``.

If you intend to listen on all interfaces and understand the implications, set the host to ``0.0.0.0``.
Otherwise Matterllo will listen on localhost and you will need to proxy requests to it.
Keep the port above 1024 and never run Matterllo as root.

.. code-block:: bash

    # these are the default values
    $ export MATTERLLO_API_HOST='localhost'
    $ export MATTERLLO_API_PORT='8080'

Trello webhook
--------------

Currently there is no graphical interface for creating webhooks in Trello.
In order to create your hook, you will need to customize the configuration file and run the ``helper.py`` once.

.. code-block:: bash

    # this part will create the necessary webhook using the Trello API.
    $ export MATTERLLO_CONFIG_FILE='path/to/config.yaml'
    $ python matterllo/scripts/helper.py --init

Launch
------
.. code-block:: bash

    # Enjoy !
    $ export MATTERLLO_CONFIG_FILE='path/to/config.yaml'
    $ python matterllo/run.py

Keep in mind that your hooks are only being forwarded while Matterllo is running, so you will want to create a daemon or service for it.
