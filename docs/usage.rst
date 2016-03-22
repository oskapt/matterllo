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

Trello webhook
--------------

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
